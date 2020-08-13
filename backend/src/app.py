# coding=utf-8
import OpenSSL.debug
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.models.entity import db
from src.models.user import User
from src.models.tree import Tree, TreeSchema
from src.models.option import Option, OptionSchema
from src.models.node import Node, NodeSchema
from src.models.option_value import OptionValue, OptionValueSchema
from src.models.decision import Decision, DecisionSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/decisions.db'
#app.config['SQLALCHEMY_ECHO'] = False
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/decision/<tree_id>')
def get_decision_framework(tree_id):
    #declare tables that are in database
    tree = Tree.query.filter_by(id = tree_id).first()
    schema = TreeSchema()
    tree_json = schema.dump(tree)
    return jsonify(tree_json)

@app.route('/decisions/')
def get_all_decisions():
    # fetching from the database
    tree_objects = db.session.query(Tree).all()

    # transforming into JSON-serializable objects
    schema = TreeSchema(many=True)
    trees = schema.dump(tree_objects)

    # serializing as JSON
    db.session.close()
    return jsonify(trees)


@app.route('/decision', methods=['POST'])
def add_exam():
    # mount decision object
    posted_decision = DecisionSchema().load(request.get_json())
    decision = Decision(**posted_decision.data, created_by="HTTP post request")
    
    options = decision.options
    option_values = decision.option_values
    tree, nodes = decision.normalize()
       
    # persist decision tree

    db.session.add(tree)
    db.session.add_all(nodes)
    db.session.add_all(options)
    db.session.add_all(option_values)
    db.session.commit()

    # return created decision tree
    new_decision = DecisionSchema().dump(decision).data
    db.session.close()
    return jsonify(new_decision), 201

"""
# check for existing optionvalues
opt_vals = db.session.query(OptionValue).all()
if len(opt_vals) == 0:
    # create and insert tree, node, option, and option value
    user = User("basic_user", "John Doe", "johndoe@email.com", "BASIC-PASSWORD" )
    session.add(user)
    session.commit()
    tree = Tree("test tree", "a simple test tree", user.id, False)
    db.session.add(tree)
    db.session.commit()
    node = Node("test node 1", "node 1 for option 1 for test tree", tree.id, db.null(), 0, current_user)
    db.session.add(node)
    db.session.commit()
    option = Option("test option 1", "option 1 for test tree", tree.id, current_user)
    db.session.add(option)
    db.session.commit()
    option_value = OptionValue(node.id, option.id, 1, 1, current_user)
    db.session.add(option_value)
    db.session.commit()
    db.session.close()

    # reload optionvalues
    opt_vals = db.session.query(OptionValue).all()

# show existing exams
print('### OptionValues:')
for opt_val in opt_vals:
    print(f'({opt_val.id}) {opt_val.node_id}  {opt_val.option_id}, w: {opt_val.weight}, v: {opt_val.value}')
print(len(opt_vals))
"""

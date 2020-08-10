# coding=utf-8
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import null

# creating the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/decisions.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.entities.entity import Session, engine, Base
from src.entities.option_tree import *
from src.entities.tree import Tree, TreeSchema
from src.entities.option import Option, OptionSchema
from src.entities.node import Node, NodeSchema
from src.entities.option_value import OptionValue, OptionValueSchema

engine.echo = True  # We want to see the SQL we're creating

db.create_all()

@app.route('/decision/<tree_id>')
def get_decision_framework(tree_id):
    #declare tables that are in database
    trees_table = Table('trees', Base.metadata, autoload=True)
    options_table = Table('options', Base.metadata, autoload=True)
    option_values_table = Table('option_values', Base.metadata, autoload=True)

    #query for objects we want
    tree = trees_table.select(trees_table.c.id == tree_id)

@app.route('/decisions/')
def get_all_decisions():
    # fetching from the database
    session = Session()
    tree_objects = session.query(Tree).all()

    # transforming into JSON-serializable objects
    schema = TreeSchema(many=True)
    trees = schema.dump(tree_objects)

    # serializing as JSON
    session.close()
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
    session = Session()

    session.add(tree)
    session.add_all(nodes)
    session.add_all(options)
    session.add_all(option_values)
    session.commit()

    # return created decision tree
    new_decision = DecisionSchema().dump(decision).data
    session.close()
    return jsonify(new_decision), 201

"""
# start session
session = Session()

# check for existing optionvalues
opt_vals = session.query(OptionValue).all()
current_user = 'Andrew'

if len(opt_vals) == 0:
    # create and insert tree, node, option, and option value
    tree = Tree("test tree", "a simple test tree", current_user)
    session.add(tree)
    session.commit()
    node = Node("test node 1", "node 1 for option 1 for test tree", tree.id, null(), 0, current_user)
    session.add(node)
    session.commit()
    option = Option("test option 1", "option 1 for test tree", tree.id, current_user)
    session.add(option)
    session.commit()
    option_value = OptionValue(node.id, option.id, 1, 1, current_user)
    session.add(option_value)
    session.commit()
    session.close()

    # reload optionvalues
    opt_vals = session.query(OptionValue).all()

# show existing exams
print('### OptionValues:')
for opt_val in opt_vals:
    print(f'({opt_val.id}) {opt_val.node_id}  {opt_val.option_id}, w: {opt_val.weight}, v: {opt_val.value}')
print(len(opt_vals))
"""

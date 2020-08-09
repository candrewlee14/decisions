# coding=utf-8
from flask import Flask, jsonify, request
from sqlalchemy import null

from src.entities.option_tree import *
from src.entities.entity import Session, engine, Base
from src.entities.tree import Tree, Tree
from src.entities.option import Option, OptionSchema
from src.entities.node import Node, NodeSchema
from src.entities.option_value import OptionValue, OptionValueSchema

# creating the Flask application
app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)

@app.route('/decision/<tree_id>')
def get_decision_framework(tree_id):


@app.route('/decision', methods=['POST'])
def add_exam():
    # mount decision object
    posted_decision = DecisionSchema().load(request.get_json())
    decision = Decision(**posted_decision.data, created_by="HTTP post request")

    # persist decision
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201
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

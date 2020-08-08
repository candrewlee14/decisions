# coding=utf-8
from sqlalchemy import null
from entities.entity import Session, engine, Base
from entities.tree import Tree
from entities.option import Option
from entities.node import Node
from entities.option_value import OptionValue

# generate database schema
Base.metadata.create_all(engine)

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
    node = Node("test node 1", "node 1 for option 1 for test tree", tree.id, null(), current_user)
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

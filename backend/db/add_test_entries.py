import sqlite3
from uuid import UUID

def get_hex_of_uuid(uuid_str: str):
    return str(UUID('{{{0}}}'.format(uuid_str)).hex)


conn = sqlite3.connect('db/decisions.db')

cur = conn.cursor()

tree_id = get_hex_of_uuid('3b6af0a1-59d0-4626-9cfc-af11909f9558')
option_id = get_hex_of_uuid('010fbb05-44a6-40f5-bd9d-0b0d8cf0540b')
node1_id = get_hex_of_uuid('bd6fbe99-dfbd-46c9-888f-20018419937e')
node2_id = get_hex_of_uuid('5f24f9cc-d215-4d67-89ce-90a84d7ea20e')
node3_id = get_hex_of_uuid('8ec3734a-5b86-4eeb-97eb-ae52e7f171dc')

#insert user
cur.execute('''INSERT OR REPLACE INTO "users" 
("id", "username", "name", "email", "password") 
VALUES ('1', 'default_user', 'John Doe', 'johndoe@email.com', 'PASSWORD1');
''')
#insert tree
cur.execute('''INSERT OR REPLACE INTO "trees" 
("id", "created_at", "updated_at", "title", "description", "created_by", "is_private") 
VALUES ('{0}', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Test Tree 1', 'Decisions tree made for testing', '1', '0');
'''.format(tree_id))
#insert option
cur.execute('''INSERT OR REPLACE INTO "options"
("id", "created_at", "updated_at", "title", "description", "tree_id")
VALUES ('{0}', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Option 1 for Test Tree', 'This is just an option!', '{1}');
'''.format(option_id, tree_id))
#insert nodes
cur.execute('''INSERT OR REPLACE INTO "main"."nodes"
("id", "created_at", "updated_at", "title", "description", "tree_id", "depth")
VALUES ('{0}', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Parent Node 1', 'Parent Node 1 for Test Decision', '{1}', 0);
'''.format(node1_id, tree_id))
cur.execute('''INSERT OR REPLACE INTO "main"."nodes"
("id", "created_at", "updated_at", "title", "description", "tree_id", "parent_id", "depth")
VALUES ('{0}', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Child Node 1', 'Child Node 1 for Test Decision', '{1}', '{2}', 1);
'''.format(node2_id, tree_id, option_id))
cur.execute('''INSERT OR REPLACE INTO "main"."nodes"
("id", "created_at", "updated_at", "title", "description", "tree_id", "parent_id", "depth")
VALUES ('{0}', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Child Node 2', 'Child Node 2 for Test Decision', '{1}', '{2}', 1);
'''.format(node3_id, tree_id, option_id))
#insert option values
cur.execute('''INSERT OR REPLACE INTO "main"."option_values"
("created_at", "updated_at", "node_id", "option_id", "weight", "value")
VALUES ('2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', '{0}', '{1}', 1, 10);
'''.format(
    node3_id, 
    option_id
))


conn.commit()
conn.close()

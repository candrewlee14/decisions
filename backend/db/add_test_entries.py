import sqlite3
conn = sqlite3.connect('db/decisions.db')

cur = conn.cursor()

#insert user
cur.execute('''INSERT OR REPLACE INTO "users" 
("id", "username", "name", "email", "password") 
VALUES ('1', 'default_user', 'John Doe', 'johndoe@email.com', 'PASSWORD1');''')
#insert tree
cur.execute('''INSERT OR REPLACE INTO "trees" 
("id", "created_at", "updated_at", "title", "description", "created_by", "is_private") 
VALUES ('3b6af0a1-59d0-4626-9cfc-af11909f9558', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Test Tree 1', 'Decisions tree made for testing', '1', '0');''')
#insert option
cur.execute('''INSERT OR REPLACE INTO "options"
("id", "created_at", "updated_at", "title", "description", "tree_id")
VALUES ('010fbb05-44a6-40f5-bd9d-0b0d8cf0540b', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Option 1 for Test Tree', 'This is just an option!', '3b6af0a1-59d0-4626-9cfc-af11909f9558');''')
#insert nodes
cur.execute('''INSERT OR REPLACE INTO "main"."nodes"
("id", "created_at", "updated_at", "title", "description", "tree_id", "depth")
VALUES ('bd6fbe99-dfbd-46c9-888f-20018419937e', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Parent Node 1', 'Parent Node 1 for Test Decision', '3b6af0a1-59d0-4626-9cfc-af11909f9558', 0);''')
cur.execute('''INSERT OR REPLACE INTO "main"."nodes"
("id", "created_at", "updated_at", "title", "description", "tree_id", "parent_id", "depth")
VALUES ('5f24f9cc-d215-4d67-89ce-90a84d7ea20e', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Child Node 1', 'Child Node 1 for Test Decision', '3b6af0a1-59d0-4626-9cfc-af11909f9558', 'bd6fbe99-dfbd-46c9-888f-20018419937e', 0);''')
cur.execute('''INSERT OR REPLACE INTO "main"."nodes"
("id", "created_at", "updated_at", "title", "description", "tree_id", "parent_id", "depth")
VALUES ('8ec3734a-5b86-4eeb-97eb-ae52e7f171dc', '2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'Child Node 2', 'Child Node 2 for Test Decision', '3b6af0a1-59d0-4626-9cfc-af11909f9558', 'bd6fbe99-dfbd-46c9-888f-20018419937e', 0);''')
#insert option values
cur.execute('''INSERT OR REPLACE INTO "main"."option_values"
("created_at", "updated_at", "node_id", "option_id", "weight", "value")
VALUES ('2020-08-11 18:46:04.247509', '2020-08-11 18:46:04.247509', 'bd6fbe99-dfbd-46c9-888f-20018419937e', '010fbb05-44a6-40f5-bd9d-0b0d8cf0540b', 1, 10);''')


conn.commit()
conn.close()

import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

new_db = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if new_db:
        print('Let us create schema')
        with open(schema_filename, 'r') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        conn.executescript("""
        insert into project (name, description, deadline)
        values ('assignments', 'Assignments - Python for Data Science', '2021-07-24');

        insert into task (details, status, deadline, project)
        values ('assignment 1', 'done', '2021-07-29', 'assignments');

        insert into task (details, status, deadline, project)
        values ('assignment 2', 'in progress', '2021-07-22', 'assignments');

        insert into task (details, status, deadline, project)
        values ('assignment 3', 'active', '2021-07-31', 'assignments');
        """)
    else:
        print('Database exists, assume schema does, too.')

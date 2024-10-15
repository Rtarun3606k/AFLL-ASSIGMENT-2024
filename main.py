from parser import parser

# Sample SQL statements
sql_statements = [
    "CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(100));",
    "INSERT INTO students (id, name) VALUES (1, 'John Doe');",
    "SELECT id, name FROM students WHERE id > 0;"
]

for statement in sql_statements:
    result = parser.parse(statement)
    print(result)
from pymilvus import connections, db

_HOST = '127.0.0.1'
_PORT = '19530'
_ROOT = "root"
_ROOT_PASSWORD = "Milvus"
_ROLE_NAME = "test_role"
_PRIVILEGE_INSERT = "Insert"

conn = connections.connect(host="127.0.0.1", port=19530)
database = db.create_database("book")

conn = connections.connect(
    host="127.0.0.1",
    port="19530",
    db_name="default"
)

db.list_database()

# Output
['default', 'book']

# NOTE: please make sure the 'foo' db has been created
db_name = "foo"
connect_to_milvus()
role.grant("Collection", "*", _PRIVILEGE_INSERT, db_name=db_name)
print(role.list_grants(db_name=db_name))
print(role.list_grant("Collection", "*", db_name=db_name))
role.revoke("Global", "*", _PRIVILEGE_INSERT, db_name=db_name)

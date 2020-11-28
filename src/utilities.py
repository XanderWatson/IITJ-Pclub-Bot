from sql import Database, Column, Table

db = Database('data.db')
users = Table(db, 'users', [
    Column('id', 'INTEGER'),
    Column('score', 'REAL'),
    Column('prev_msg', 'INTEGER'),
    Column('tod_msg', 'INTEGER')
])

total_msg = Table(db, 'total_msg', [
    Column('id', 'INTEGER'),
    Column('msg', 'INTEGER'),
    Column('tod_msg', 'INTEGER')
])

def add_user(id_str):
    users.add_element(id_str, {'score': 50})


def update_user_msg_count(id_str):
    if users.get(id_str) is None:
        add_user(id_str)
    prev_count = users.get(id_str, "tod_msg")
    users.update(id_str, {"tod_msg": prev_count[0]+1})
    update_server_msg_count()


def update_server_msg_count():
    if total_msg.get(1) is None:
        total_msg.add_element(1) 
    prev_count = users.get(1, "tod_msg")
    users.update(id_str, {"tod_msg": prev_count[0]+1})
    

from ..db.users import users

def insert_user(user_id,user_name):
    if user_id in users:
        return "User already exists"
    users[user_id] = user_name
    return "success"
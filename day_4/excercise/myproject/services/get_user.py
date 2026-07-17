from ..db.users import users

def get_user(user_id):
    if user_id in user_id:
        return users[user_id]
    return "User not found"
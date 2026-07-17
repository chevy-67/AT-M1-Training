from ..db.users import users

def show_user():
    for user in users:
        print(user[0],'-',user[1])
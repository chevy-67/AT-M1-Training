users = {101:'Abi',102:'Akil',103:'Ken',104:'San'}

def get_user(user_id):
    if user_id in user_id:
        return users[user_id]
    return "User not found"

def insert_user(user_id,user_name):
    if user_id in users:
        return "User already exists"
    users[user_id] = user_name
    return "success"

def show_user():
    for user in users:
        print(user[0],'-',user[1])

while True:
    print('1.Find user\n2.Add user\n3.Show user\n4.Exit')
    inp = int(input("Enter choice"))
    if inp==1:
        id = int(input("Enter user id : "))
        print(get_user(id))
    elif inp==2:
        id = int(input("Enter user id : "))
        name = input("Enter user name : ")
        insert_user(id,name)
    elif inp==3:
        show_user()
    elif inp==4:
        break
    else:
        print("Invalid option")
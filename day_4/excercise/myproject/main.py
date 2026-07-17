from api import fetch_user as show_user
from services import add_user as insert_user
from services import get_user

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
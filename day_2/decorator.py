def give_credits(func):
    def wrapper(*args):
        print("Welcome you all,the winners are")
        func(*args)
        print("Thank you...")
    return wrapper

@give_credits
def winner(names):
    for name in names:
        print(name)

names = ['abi','sam','ken','jim']
winner(names)
import time

def printName():
    print(__name__)

if __name__=='__main__':
    print("I'm running on my own")
else:
    print("Someone running me")

time.sleep(5)
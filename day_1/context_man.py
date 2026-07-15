def read(filename):
    with open(filename,'r') as main:
        for line in main:
            print(line)

def write(text,filename):
    with open(filename,'a') as file:
        file.write(text)
        file.write('\n')

print_st = "print(\"hello word\")"
filename = "main.py"
write(print_st,filename)
read(filename)
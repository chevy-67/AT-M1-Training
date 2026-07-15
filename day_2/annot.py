def merge(name: str,year: int)->str:
    title = name+' ('+str(year)+')'
    return title

def add(a:int,b:float)->str:
    return str(a+b)

print(add(1,1.1))

movie1 = merge('anbe sivam',2002)
print(movie1)
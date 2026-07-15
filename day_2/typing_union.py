from typing import Union

def add(a:Union[int,float],b:Union[str,int])->float:
    return float(a+b)

print(add(0.1,0.2))
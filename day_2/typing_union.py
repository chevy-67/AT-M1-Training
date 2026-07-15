from typing import Union,Optional

def product(a:int | float,b:int | float)->Optional[float]:
    #return a*b
    return float(a*b)

def add(a:Union[int,float],b:Union[str,int])->float:
    """
    Calculates sum of two numbers

    Input :
        a : either int or float
        b : either int or string

    Returns:
        sum of two nums in float
    """
    return float(a+b)

print(add(0.1,0.2))
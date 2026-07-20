def add(a,b):
    return a+b

def sort_ar(ar):
    ar_sorted = sorted(ar)
    return ar_sorted 


def test():
    assert add(1,2) == 3
    assert sort_ar([1,5,2,3,7,2]) == [1,2,2,3,5,7]
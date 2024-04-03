from typing import Callable,List
def multiple(m, n):
    if m < n:
        return False
    elif m == n:
        return True
    #print(m - n)
    return multiple(m - n, n)

# Exemples
#print(multiple(10, 2))  #  True
'''print(multiple(7, 3))   #  False 
print(multiple(15, 3))  # TRUE'''
 

def diviseursR(m, n):
    if n > m / 2:
        return []
    elif multiple(m,n) : #m % n == 0
        return [n] + diviseursR(m, n + 1) 
    return diviseursR(m, n + 1)
 
diviseurs: Callable[[int], List[int]] = lambda m: diviseursR(m, 1)  

premier: Callable[[int], bool] = lambda m: diviseurs(m) == [1]
print(premier(15))  # ex :12 [1, 2, 3, 4, 6]

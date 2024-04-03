def multiple(m, n):
    if m < n:
        return False
    elif m == n:
        return True
    print(m - n)
    return multiple(m - n, n)

# Exemples
print(multiple(10, 2))  #  True
'''print(multiple(7, 3))   #  False 
print(multiple(15, 3))  # TRUE'''
 
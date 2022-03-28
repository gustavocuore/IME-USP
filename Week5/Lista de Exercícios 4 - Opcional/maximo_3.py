def maximo(x,y,z):
    if x != y and y != z:
        if x > y and x > z:
            return x
        if y > x and y > z:
            return y
        else:
            return z
    if x == y and x != z:
        if x > z:
            return x
        else:
            return z

    if y == z and y != x:
        if y > x:
            return y
        else:
            return x
    else:
        return x
    

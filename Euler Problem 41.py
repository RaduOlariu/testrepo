import math
import itertools as it

def is_prime(x):
    if x % 2 == 0:
        return False
    elif x % 3 ==0:
        return False
    elif ((x-1) % 6 != 0) and ((x + 1) % 6 != 0):
        return False
    else:
        for i in range(5,math.floor(x/2)):
            if x % i == 0:
                return False
        return True

def Tuple_to_Int(tup):
    result = 0
    for i in range(0,len(tup)):
        result = result + tup[i] * 10 ** (len(tup)-(i+1))
    return result

solution = 0

for i in range(7,1,-1):
    for element in it.permutations(range(i,0,-1)):
        if element[len(element)-1] in {2,4,5,6,8}:
            continue
        if is_prime(Tuple_to_Int(element)):
            solution = Tuple_to_Int(element)
            print(solution)
            break
    if solution != 0:
        break

print(solution)

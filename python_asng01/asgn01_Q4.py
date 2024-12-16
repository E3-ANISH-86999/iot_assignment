def max_fn(p1:int, p2:int, p3:int):
    if p1 > p2:
        if p1 > p3:
            return p1
    elif p2 > p3:
        return p2
    else: 
        return p3

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))

max = max_fn(a, b, c)

print(f"Max number = {max}")   

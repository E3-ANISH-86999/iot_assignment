list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def fact_fn(p1:int):
    i = 1
    fact = 1
    while i <= p1:
        fact = fact * i
        i += 1

    return fact

for num in list:
    factorial = fact_fn(num) 
    print(f"Factorial of {num}: {factorial}")





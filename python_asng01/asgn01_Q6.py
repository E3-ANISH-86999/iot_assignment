num = int(input("Enter a number: "))

def fact_fn(p1:int):
    i = 1
    fact = 1
    while i <= p1:
        fact = fact * i
        i += 1

    return fact

factorial = fact_fn(num) 
print(f"Factorial of {num}: {factorial}")





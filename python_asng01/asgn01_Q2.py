num = int(input("Enter a 4-digit number: "))
temp = num

i = 4   
while i > 0:
    place_val = temp % (10 ** i)
    i -= 1
    place_val = int(place_val / (10 ** i))
    print(f"face value: {place_val}") 
    place_val = place_val *( 10 ** i)
    print(f"place value: {place_val}") 

num1 = temp % 10
num1 = int(num1 / 1)

num2 = temp % 100
num2 = int(num2 / 10)

num3 = temp % 1000
num3 = int(num3 / 100)

num4 = temp % 10000
num4 = int(num4 / 1000)

rev = (num1 * 1000) + (num2 * 100) + (num3 * 10) + num4
print(f"Reverse Number: {rev}")







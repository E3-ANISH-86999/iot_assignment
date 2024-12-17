def simple_interest(p:int, r:int, t:int):
    return ((p*r*t) / 100)

principal_amt = int(input("Enter principal amount: "))
rate_of_interest = int(input("Enter rate of interest: "))
Time_in_years = int(input("Enter time in years: "))

si = simple_interest(principal_amt, rate_of_interest, Time_in_years)
print(f"Simple interest = {si}")



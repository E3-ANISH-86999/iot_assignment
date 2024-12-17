def compound_interest(p:int, r:int, t:int):
    return round((p * ((1 + (r/100))**t)), 2)


principal_amt = int(input("Enter principal amount: "))
rate_of_interest = int(input("Enter rate of interest: "))
Time_in_years = int(input("Enter time in years: "))

ci = compound_interest(principal_amt, rate_of_interest, Time_in_years)
print(f"compound interest = {ci}")



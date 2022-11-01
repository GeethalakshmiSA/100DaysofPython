# PROBLEM STATEMENT - Calculate Simple Interest
# Formula of Simple Interest = (Principle * Time * Rate)/100

principle = float(input("Enter the principle amount = "))
timePeriod = float(input("Enter the time period taken in years = "))
rateOfInterest = float(input("Enter the rate of interest = "))

simpleInterest = (principle * timePeriod * rateOfInterest) / 100

print("Simple Interest is ", simpleInterest)

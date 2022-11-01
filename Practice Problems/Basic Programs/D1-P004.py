# PROBLEM STATEMENT - Calculate Simple Interest & Compund Interest
# Formula of Simple Interest = (Principle * Time * Rate)/100
# Formula of Compound Interest = Amount - Principle where Amount =  Principle (1 + Rate/100) ** Time

def simpleInterest(principle, timePeriod, rateOfInterest):
    interest = (principle * timePeriod * rateOfInterest) / 100
    return interest

def compoundInterest(principle, timePeriod, rateOfInterest):
    amount = principle * (1 + (rateOfInterest/100)) ** timePeriod
    interest = amount - principle
    return interest


principle = float(input("Enter the principle amount = "))
timePeriod = float(input("Enter the time period taken in years = "))
rateOfInterest = float(input("Enter the rate of interest = "))

print("Simple Interest is ", simpleInterest(principle, timePeriod, rateOfInterest))
print("Compound Interest is ", compoundInterest(principle, timePeriod, rateOfInterest))

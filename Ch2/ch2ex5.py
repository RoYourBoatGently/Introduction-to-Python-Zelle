# Chapter 2 Exercse 5
# A program to compute the value of an investment
# carried out x years into the future - where x is specified by the user

def main():

    print("This program calculates the future value")
    print("of an investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in ", years, " years is ", round(principal, 2))
    
    
main()

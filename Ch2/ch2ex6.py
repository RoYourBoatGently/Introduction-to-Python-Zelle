# Chapter 2 Exercse 6
# A program to compute the value of an investment with a compound interest rate

def main():

    print("This program calculates the future value")
    print("of an investment.")
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter the number of times that the interest rate is compounded: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years*periods):
        principal = principal * (1 + rate/periods)

    print("The value in ", years, " years is ", round(principal, 2))
    
    
main()

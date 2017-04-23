# Chapter 2 Exercse 6
# Converts farenheit to celsius

def main():
    print("This program converts farenheit into celsius.")
    f = eval(input("Please enter a temperature in degrees farenehit: "))
    c = (f - 32) * (5/9)
    print("The temperature",f,"°F is",round(c,1),"°C")
    
    

main()

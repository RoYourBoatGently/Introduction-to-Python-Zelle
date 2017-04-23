#convert.py
# A program to convert celsius into farenheit

def main():

    print("Welcome to temperature converter. This program converts degrees celsius into")
    print("degrees farenheit. If you're an American abroad you'll no longer have any worries\n")
    farenheit = eval(input("Please enter the temperature in degrees farenheit: "))
    celsius = (5/9) * (farenheit - 32)
    print("The temperature ", int(farenheit), " degress farenheit is ", int(celsius), " degrees celsius")
    print("I hope you feel enlightened, have a pleasent day.")
    
main()

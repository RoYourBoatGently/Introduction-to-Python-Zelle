# Chapter 2 Exercse 3
# A program that enables 5 conversations of farenheit to celsius

def main():

    print("Welcome to temperature converter. This program converts degrees celsius into")
    print("degrees farenheit. If you're an American abroad you'll no longer have any worries\n")
    for i in range(5):
        farenheit = eval(input("Please enter the temperature in degrees farenheit: "))
        celsius = (5/9) * (farenheit - 32)
        print("The temperature ", int(farenheit), " degress farenheit is ", int(celsius), " degrees celsius")
    
    print("I hope you feel enlightened, have a pleasent day.")
    
main()

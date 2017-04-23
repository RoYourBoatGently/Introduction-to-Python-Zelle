# Chapter 2 Exercse 4
# Prints a table from 10 to 100 degrees of farenheit to celsius conversions

def main():

    print("Welcome to temperature converter. This program shows you a table of degrees farenheit")
    print("for every 10 degrees celsius. If you're an American abroad you'll no longer have any worries\n")
    print("Celsius(°C)\tFarenheit(°F)")
    for c in range(10,110,10):
        
        f = (9/5) * c  + 32
        print(c, f, sep='\t\t')
    
    print("I hope you feel enlightened, have a pleasent day.")
    
main()

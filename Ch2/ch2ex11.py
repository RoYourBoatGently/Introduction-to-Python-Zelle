# Chapter 2 Exercse 11
# Interactive python calculator program, x / 0 to quit

def main():
    for i in range(100):
        expression = eval(input("Please enter an expression to calculate: "))
        print("The answer is: ",expression)
    

main()

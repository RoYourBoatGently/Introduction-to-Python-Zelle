# Chapter 2 Exercse 9
# Converts km to miles

def main():
    print("This program converts kilometres into miles")
    k = eval(input("Please enter a distance in kilometres: "))
    m = k / 1.609344
    print("The distance",k,"km is",round(m,1),"miles")
    
    

main()

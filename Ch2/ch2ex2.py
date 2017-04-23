# Chapter 2 Exercse 2
# A program that takes the average of 3 numbers

def main():
    print ("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Enter three scores seperated by a comma: "))
    average = (score1 + score2 + score3) / 3
    print ("The average score is: ", round(average, 2))
    
    
main()

# ✅↓ Write your code here ↓✅


def number_of_bottles():
    num = 99
    for i in range (0,20):
     print (num," bottles of milk of the wall,",num," bottles of milk")
     num=num-1
     print ("Take one down and pass it around,",num,"bottles of milk on the wall")
     if num==1:
        print (num," bottle of milk of the wall,",num," bottle of milk")
        num=num-1
        print ("Go to thestore and buy some more, 99 bottles of milk on the wall")

number_of_bottles()
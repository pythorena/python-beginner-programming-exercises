def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for num in range (0,101):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%5==0:
            print("Buzz")
        elif num%3==0:
            print("Fizz")
        else: print(num)
# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()

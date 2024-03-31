# List Value Square Sum
def p(x):
    print("Answer is: ", x)
temp = 0
for nums in [3,4]:
    temp = (temp + (nums**2)) #recall: ** means exponent
p(temp)

#break statements

for numbers in range(10):
    if numbers ==5:
        break
    print(numbers, end=" ")

#continue statement / range

for r in range(15):
    if r%2==0:
        continue
        p(r)

#prime number 1-100

def prime(n):
    flag = 0
    temp = 2
    while temp <= n/2:
        if n%temp==0:
            flag = 1
            break
        temp += 1
    if flag ==0:
        print(n, end=" ")
        
for numbers in range(2, 100):
    prime(numbers)
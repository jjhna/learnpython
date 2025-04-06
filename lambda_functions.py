a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)

l = [2,4,7,3,14,19]
for i in l:
    # your code here
    printsum = lambda a : a % 2 == 1
    print(printsum(i))
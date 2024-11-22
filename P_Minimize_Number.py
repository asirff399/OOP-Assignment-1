n =int(input())

a = list(map(int,input().split()))

def allEven(a):
    for num in a:
        if num % 2 != 0:
            return False
    return True

cnt = 0
while allEven(a):
    newA = []
    for num in a:
        newA.append(num // 2)
    a = newA
    cnt +=1

if cnt > 0 :
    print(cnt)
else:
    print(0)

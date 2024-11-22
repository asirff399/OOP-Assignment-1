def maxSplit(s):
    cnt_l = 0
    cnt_r = 0
    balance = []
    curr = ""

    for c in s:
        if c == 'L':
            cnt_l += 1
        elif c == 'R':
            cnt_r += 1
            
        curr += c

        if cnt_l == cnt_r:
            balance.append(curr)
            curr = ""
            cnt_l = 0
            cnt_r = 0
    return len(balance),balance

s = input().strip()

maxS,balance = maxSplit(s)
print (maxS)
for s in balance:
    print(s)
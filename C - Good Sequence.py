def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    mp = {}
    for e in arr:
        if e in mp:
            mp[e] += 1
        else:
            mp[e] = 1

    num = 0
    for key, val in mp.items():
        if key == val:
            continue
        else:
            if key < val:
                num += val - key
            else:
                num += val
    print(num)

if __name__ == "__main__":
    solve()

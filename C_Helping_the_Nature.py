from sys import stdin, stdout
 
 
t = int(stdin.readline())
for tt in range(t):
    n = int(stdin.readline())
    a = [int(s) for s in stdin.readline().split()]
 
 
    left_dec, right_dec = 0, 0
    res = 0
 
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            right_dec += a[i + 1] - a[i]
            res += a[i + 1] - a[i]
        elif a[i] > a[i + 1]:
            left_dec += a[i] - a[i + 1]
            res += a[i] - a[i + 1]
 
    res += abs(a[0] - left_dec)
    print(res)
 
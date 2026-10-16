import sys
import math

def solve():
    data = sys.stdin.read().strip().split()
    T = int(data[0])
    idx = 1
    res = []
    for _ in range(T):
        N = int(data[idx]); K = int(data[idx+1])
        idx += 2
        
        if N > K:
            res.append("0 1")
            continue
        
        A = (K - N + 1) * pow(K + 1, N - 1)
        B = pow(K, N)
        
        g = math.gcd(A, B)
        res.append(f"{A//g} {B//g}")
    
    print('\n'.join(res))

if __name__ == "__main__":
    solve()
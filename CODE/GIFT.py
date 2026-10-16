import sys

def solve():
    data = sys.stdin.read().split()
    p, q, r = map(int, data[:3])
    s = ''.join(data[3:])

    good = [[[False]*r for _ in range(q)] for __ in range(p)]
    for z in range(r):
        for y in range(q):
            for x in range(p):
                idx = z * p * q + y * p + x
                if s[idx] == 'N':
                    good[x][y][z] = True

    same = [[[0]*(r+1) for _ in range(q)] for __ in range(p)]
    for z in range(r-1, -1, -1):
        for y in range(q):
            for x in range(p):
                if good[x][y][z]:
                    same[x][y][z] = same[x][y][z+1] + 1
                else:
                    same[x][y][z] = 0
    
    max_val = 0
    def check(h):
        best = 0
        stack = []
        for i, height in enumerate(h + [0]):
            start = i
            while stack and stack[-1][1] > height:
                idx, b = stack.pop()
                width = i - idx      
                a = width             
                side = min(a, b)     
                best = max(best, 4 * side * max(a, b))
                start = idx
            stack.append((start, height))
        return best

    for z in range(r):
        for y1 in range(q):
            h = [same[x][y1][z] for x in range(p)]
            max_val = max(max_val, check(h))
            for y2 in range(y1+1, q):
                a_side = y2 - y1 + 1  
                for x in range(p):
                    h[x] = min(h[x], same[x][y2][z])
                for x in range(p):
                    if h[x] >= a_side:
                        pass
                max_val = max(max_val, 4 * a_side * max(h))
    
    print(max_val)

if __name__ == "__main__":
    solve()
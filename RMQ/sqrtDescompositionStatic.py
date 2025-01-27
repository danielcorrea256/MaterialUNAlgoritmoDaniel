import sys
input = sys.stdin.readline

INF = 10**9 + 1
block_size = 400

n, q = map(int, input().split())
a = list(map(int, input().split()))

block_number = (n + block_size - 1) // block_size

b = [INF] * block_number

for i in range(n):
    block_index = i // block_size
    b[block_index] = min(b[block_index], a[i])

answers = [""] * q

for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    j = l
    ans = INF
 
    while j <= r:
        if j % block_size == 0 and j + block_size - 1 <= r:
            ans = min(ans, b[j // block_size])
            j += block_size
        else:
            ans = min(ans, a[j])
            j += 1
    
    answers[i] = str(ans)

# Output all answers
sys.stdout.write("\n".join(answers))
sys.stdout.write("\n")
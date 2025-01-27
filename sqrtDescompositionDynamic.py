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

answers = []

for i in range(q):
    type, x, y = map(int, input().split())

    if type == 1:
        k = x - 1
        u = y

        a[k] = u
        block_index = k // block_size 
        
        b[block_index] = INF
        for j in range(block_index*block_size, min((block_index+1) * block_size , n)):
            b[block_index] = min(b[block_index], a[j])
    else:
        l = x - 1
        r = y - 1

        j = l
        ans = INF
    
        while j <= r:
            if j % block_size == 0 and j + block_size - 1 <= r:
                ans = min(ans, b[j // block_size])
                j += block_size
            else:
                ans = min(ans, a[j])
                j += 1
        
        answers.append(str(ans))

# Output all answers
sys.stdout.write("\n".join(answers))
sys.stdout.write("\n")
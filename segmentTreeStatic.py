import sys

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # allocate space for segment tree
        self.INF = 10**9 + 1
        self.build(arr, 1, 0, self.n - 1)
    
    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, v*2, tl, tm)
            self.build(arr, v*2 + 1, tm + 1, tr)
            self.tree[v] = min(self.tree[v*2], self.tree[v*2 + 1])
    
    def query_range(self, v, tl, tr, l, r):
        if l > r:
            return self.INF
        if tl == l and tr == r:
            return self.tree[v]
        tm = (tl + tr) // 2
        left_min = self.query_range(v*2, tl, tm, l, min(r, tm))
        right_min = self.query_range(v*2 + 1, tm + 1, tr, max(l, tm + 1), r)
        return min(left_min, right_min)
    
    def query(self, l, r):
        """Public method to query the minimum on [l, r]."""
        return self.query_range(1, 0, self.n - 1, l, r)


data = sys.stdin.read().strip().split()

n, q = map(int, data[:2])
idx = 2

# read the array
arr = list(map(int, data[idx:idx + n]))
idx += n

# build the segment tree
seg_tree = SegmentTree(arr)

# process queries
outputs = []
for _ in range(q):
    l = int(data[idx]); r = int(data[idx+1])
    idx += 2
    
    # Convert to zero-based indexing
    l -= 1
    r -= 1
    
    answer = seg_tree.query(l, r)
    outputs.append(str(answer))

# print all results
print("\n".join(outputs))
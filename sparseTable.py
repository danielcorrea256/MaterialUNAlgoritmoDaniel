import sys

class RMQ:
    """
    A class that builds and queries a Sparse Table for RMQ (Range Minimum Query).
    
    Time Complexity:
      - Build: O(n log n)
      - Query: O(1) per query
    """
    def __init__(self, arr):
        """
        Constructor that takes in an array (list) of integers and builds the Sparse Table.
        """
        self.arr = arr
        self.n = len(arr)
        
        # Precompute logs for 1..n to enable O(1) lookups for the largest power of two.
        self.logs = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.logs[i] = self.logs[i // 2] + 1
        
        # Maximum power of 2 needed
        self.K = self.logs[self.n]
        
        # Sparse Table array: st[k][i] will store the minimum of the interval
        # starting at i, of length 2^k
        self.st = [[0] * self.n for _ in range(self.K + 1)]
        
        # Build the sparse table
        self._build()
    
    def _build(self):
        """
        Internal method to build the sparse table in O(n log n).
        """
        # Initialize level-0 with the original array
        for i in range(self.n):
            self.st[0][i] = self.arr[i]
        
        j = 1
        while (1 << j) <= self.n:
            length = 1 << j     # 2^j
            half = length >> 1  # 2^(j-1)
            
            i = 0
            while i + length - 1 < self.n:
                self.st[j][i] = min(self.st[j - 1][i],
                                    self.st[j - 1][i + half])
                i += 1
            j += 1
    
    def query(self, left, right):
        """
        Returns the minimum value in the range [left, right] (0-based indices),
        in O(1).
        """
        length = right - left + 1
        k = self.logs[length]
        # Compare the two overlapping blocks that cover [left, right]
        return min(self.st[k][left], 
                   self.st[k][right - (1 << k) + 1])


data = sys.stdin.read().strip().split()
n, q = map(int, data[:2])
a = list(map(int, data[2:2+n]))

sparse_table = RMQ(a)
answers = []
idx = 2 + n

for _ in range(q):
    l = int(data[idx]); r = int(data[idx+1])
    idx += 2
    # Convert to 0-based
    l -= 1
    r -= 1
    ans = sparse_table.query(l, r)
    answers.append(str(ans))

# Print all answers
sys.stdout.write("\n".join(answers))
sys.stdout.write("\n")
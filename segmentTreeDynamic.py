class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.INF = 10**9 + 1
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, v, tl, tr):
        if tl == tr:
            # Leaf node
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            # Build left child
            self.build(arr, 2 * v, tl, tm)
            # Build right child
            self.build(arr, 2 * v + 1, tm + 1, tr)
            # Internal node is the min of its children
            self.tree[v] = min(self.tree[2 * v], self.tree[2 * v + 1])

    def query_range(self, v, tl, tr, l, r):
        """Return minimum value in the range [l, r]."""
        if l > r:
            return self.INF
        if tl == l and tr == r:
            return self.tree[v]

        tm = (tl + tr) // 2
        left_min = self.query_range(2 * v,     tl,     tm, l,            min(r, tm))
        right_min = self.query_range(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        return min(left_min, right_min)

    def query(self, l, r):
        """Public method to query the minimum on [l, r]."""
        return self.query_range(1, 0, self.n - 1, l, r)

    def update_range(self, v, tl, tr, pos, new_val):
        """Update the value at index `pos` to `new_val`."""
        if tl == tr:
            # Leaf node
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                # Update left child
                self.update_range(2 * v, tl, tm, pos, new_val)
            else:
                # Update right child
                self.update_range(2 * v + 1, tm + 1, tr, pos, new_val)
            # Internal node is the min of its children
            self.tree[v] = min(self.tree[2 * v], self.tree[2 * v + 1])

    def update(self, pos, new_val):
        """Public method to update the value at index `pos`."""
        self.update_range(1, 0, self.n - 1, pos, new_val)


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n, q = map(int, data[:2])
    arr = list(map(int, data[2:2 + n]))

    # Build the segment tree
    seg_tree = SegmentTree(arr)
    
    index = 2 + n  # Start reading queries
    output = []
    for _ in range(q):
        query_type = int(data[index])
        index += 1

        if query_type == 1:
            # Update query: update position k to value u
            k = int(data[index])
            u = int(data[index + 1])
            index += 2

            k -= 1  # convert to zero-based index
            seg_tree.update(k, u)
        else:
            # Range-minimum query: get min in [l, r]
            l = int(data[index])
            r = int(data[index + 1])
            index += 2

            l -= 1  # convert to zero-based index
            r -= 1
            ans = seg_tree.query(l, r)
            output.append(str(ans))

    # Print results for all range queries
    print("\n".join(output))


if __name__ == "__main__":
    main()
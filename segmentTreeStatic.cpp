#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    vector<int> tree;
    int n;
    int INF = 1e9 + 1;

    SegmentTree(vector<int>& a) : n(a.size()), tree(4 * a.size()) {
        build(a, 1, 0, n - 1);
    }

    void build(vector<int>& a, int v, int tl, int tr) {
        if (tl == tr) {
            tree[v] = a[tl];
        }
        else {
            int tm = (tl + tr) / 2;
            build(a, v*2, tl, tm);
            build(a, v*2 + 1, tm + 1, tr);
            tree[v] = min(tree[v*2], tree[v*2 + 1]);
        }
    }

    int query(int v, int tl, int tr, int l, int r) {
        if (l > r) {
            return INF;
        }
        else if (tl == l && tr == r) {
            return tree[v];
        }
        else {
            int tm = (tl + tr) / 2;
            return min(
                query(2*v, tl, tm, l, min(r, tm)), 
                query(2*v + 1, tm + 1, tr, max(l, tm + 1), r)
            );
        }
    }

    int query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    for (int &ai : a) cin >> ai;

    SegmentTree tree(a);
    
    while (q--) {
        int l, r;
        scanf("%d %d", &l, &r);

        l--, r--;

        int ans = tree.query(l, r);
        printf("%d\n", ans);
    }
}
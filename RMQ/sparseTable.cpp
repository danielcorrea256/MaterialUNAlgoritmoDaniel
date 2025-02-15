#include <bits/stdc++.h>
using namespace std;

// Code From https://github.com/ahoraSoyPeor/notebook_descomUNAL

struct RMQ {
    vector<vector<int>> table;
    RMQ(vector<int> &v) : table(20, vector<int>(v.size())) {
        int n = v.size();
        for (int i = 0; i < n; i++) table[0][i] = v[i];
        for (int j = 1; (1<<j) <= n; j++)
            for (int i = 0; i + (1<<j-1) < n; i++)
                table[j][i] = min(table[j-1][i], table[j-1][i + (1<<j-1)]);
    }
    int query(int a, int b) {
        int j = 31 - __builtin_clz(b-a+1);
        return min(table[j][a], table[j][b-(1<<j)+1]);
    }
};

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    for (int &ai : a) cin >> ai;

    RMQ sparse_table(a);

    while (q--) {
        int l, r;
        scanf("%d %d", &l, &r);
        
        l--, r--;

        int ans = sparse_table.query(l, r);
        printf("%d\n", ans);
    }
}
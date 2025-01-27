#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9 + 1;

int main() {
    int n, q;
    cin >> n >> q;

    int a[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    int s = sqrt(n) + 1;
    int b[s];
    for (int i = 0; i < s; i++)
        b[i] = INF;

    for (int i = 0; i < n; i++)
        b[i / s] = min(b[i / s], a[i]);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 1) {
            int k, u;
            scanf("%d %d", &k, &u);

            k--;

            a[k] = u;

            int block_index = k / s;
            b[block_index] = INF;

            for (int i = block_index*s; i < min(n, (block_index+1)*s); i++)
                b[block_index] = min(b[block_index], a[i]);
        }
        else {
            int l, r;
            scanf("%d %d", &l, &r);
            
            l--, r--;

            int ans = INF;
            int i = l;

            while (i <= r) {
                if (i % s == 0 && i + s - 1 <= r) {
                    ans = min(ans, b[i / s]);
                    i += s;
                }
                else {
                    ans = min(ans, a[i]);
                    i++;
                }
            }

            printf("%d\n", ans);
        }
    }
}
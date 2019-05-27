#include <bits/stdc++.h>

using namespace std;
int diagonalDifference(vector<vector<int>> ) ;

// Complete the diagonalDifference function below.
int diagonalDifference(vector<vector<int>> arr) {
                   

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;

    vector<vector<int>> arr(n);
    for (int i = 1; i <= n; i++) {
        arr[i].resize(n);

        for (int j = 1; j <=n; j++) {
            cin >> arr[i][j];
        }

    }

    int result = diagonalDifference(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}



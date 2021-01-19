#include <iostream>
#include <cstdio>
using namespace std;
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0, 0, 1, -1 };
int T, M, N, K;
bool map[51][51];
bool isvisited[51][51];

void dfs(int x, int y) {
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx >= 0 && ny >= 0 && nx < N && ny < M && !isvisited[nx][ny] && map[nx][ny]) {
			isvisited[nx][ny] = true;
			dfs(nx, ny);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> T;
	while (T--) {
		int insect = 0;
		cin >> N >> M >> K;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				isvisited[i][j] = false;
				map[i][j] = false;
			}
		}

		while (K--) {
			int X, Y;
			cin >> X >> Y;
			map[X][Y] = true;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] && !isvisited[i][j]) {
					dfs(i, j);
					insect++;
				}
			}
		}
		cout << insect << '\n';
	}

}

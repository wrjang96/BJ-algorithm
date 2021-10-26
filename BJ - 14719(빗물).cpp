#include<iostream>
#include<queue>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>

using namespace std;

int H, W;
int cnt;

void init() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
}

int main() {
	init();
	cin >> H >> W;
	int arr[501][501] = { };
	for (int i = 0; i < W; i++) {
		int temp_num;
		cin >> temp_num;
		for (int j = H; j >= H - temp_num; j--) {
			arr[j][i] +=1;
		}
	}
	int cnt = 0;
	for (int i = 0; i < H; i++) {
		bool flag = false;
		int temp_cnt = 0;
		for (int j = 0; j < W; j++) {
			if(flag == true && arr[i][j] == 0){
				temp_cnt +=1;
			}
			else if(flag == true && arr[i][j] == 1){
				cnt += temp_cnt;
				temp_cnt = 0;
			}
			else if(flag == false && arr[i][j] == 1){
				flag = true;
			}
		}
	}
	printf("%d", cnt);
	return 0;
}

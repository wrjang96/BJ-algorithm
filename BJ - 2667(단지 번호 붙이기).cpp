#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>


#define MAX 25
using namespace std;
int graph[MAX][MAX] = {0,};
bool visited[MAX][MAX]= {false,};
int complex_num = 0; 
priority_queue <int, vector<int>, greater<int> > my_q;
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

void init(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
}
void bfs(int N, int x, int y){
	queue< pair<int, int> > q; 
	q.push(make_pair(x, y));
	visited[x][y] = true;
	int temp_house_num = 1;	
	while(!q.empty()){
		int tx = q.front().first;
		int ty = q.front().second;
		q.pop();
		for(int i = 0; i <4; i++){
			int nx = tx + dx[i];
			int ny = ty + dy[i];
			if (0<= nx && nx < N && 0<=ny && ny<N && visited[nx][ny] == false && graph[nx][ny] == 1){
				q.push(make_pair(nx,ny));
				visited[nx][ny] = true;
				temp_house_num +=1;
			}
		}
	}
	my_q.push(temp_house_num);
}

int main(){
	init();
	int N ;
	scanf("%d", &N);
	for(int i=0; i < N; i ++){
		for (int j = 0;j < N; j ++){
			scanf("%1d", &graph[i][j]);
		}
	}
	for(int i=0; i < N; i ++){
		for (int j = 0;j < N; j ++){
			if(graph[i][j] == 1 && visited[i][j] == false){
				bfs(N, i,j);
				complex_num++;
			}
		}
	}
	printf("%d\n", complex_num);
	while(!my_q.empty()){
		printf("%d\n", my_q.top());
		my_q.pop();
	}
	
}

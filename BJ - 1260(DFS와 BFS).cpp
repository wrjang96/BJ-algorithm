#include <iostream>
#include <queue>
#include <cstring>


using namespace std;
queue<int> my_q;
int map[1001][1001] ={0,};
bool visited[1001]={false,};
int N,M,V;

void dfs(int x){
	cout<<x<<' ';
	visited[x] = true;
	for(int i=1; i<N+1; i++){
		if(visited[i]==false&& map[x][i] ==1){
				dfs(i);
		}
	}
	
}
void bfs(){
	my_q.push(V);
	visited[V] = true;
	while(!my_q.empty()){			
		int temp = my_q.front();
		cout<<temp<<' ';
		for(int i=1;i<N+1;i++){
			if(visited[i]==false&& map[temp][i] ==1){
				my_q.push(i);
				visited[i] = true;
			}
		}
		my_q.pop();
	}
}

int main(int argc, char** argv) {

	cin>>N>>M>>V;
	while(M--){
		int fromv,tov;
		cin>>fromv>>tov;
		map[fromv][tov]=1;
		map[tov][fromv]=1;
	}

	dfs(V);
	cout<<'\n';
	memset(visited,false,sizeof(visited));
	bfs();
	return 0;
}

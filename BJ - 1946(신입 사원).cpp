#include <iostream>
#include <algorithm>
using namespace std;
const int MAX = 100000;
int N;
pair<int, int> arr[MAX];

int main(){
	int testcase;
	cin>>testcase;
	while(testcase--){
		cin>>N;
		for(int i =0; i<N; i++){
			cin>>arr[i].first>>arr[i].second;
		}
		sort(arr,arr+N);
		int result =1;
		int flag = arr[0].second;
		for(int i =1; i<N; i++){
			if(arr[i].second<flag){
				result++;
				flag = arr[i].second;
			}
		}
		cout<<result<<'\n';
	}
} 
/*
#include <iostream>
#include <algorithm>
using namespace std;
const int MAX = 100000;
int N;
pair<int, int> arr[MAX];
	
int main(int argc, char** argv) {
	int testcase;
	cin>>testcase;
	while(testcase--){
		int N;
		cin>>N;
		for(int i =0; i<N;i++){
			cin>>arr[i].first>>arr[i].second;
		}
		sort(arr, arr+N);
		int result = 1;
		int flag = arr[0].second
		for(int i =1; i<N; i++){
			if(arr[i].second<flag){
				result++;
				flag = arr[i].second;
			}
		}
		cout<<result;
	}
	return 0;
}
*/

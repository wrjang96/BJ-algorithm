#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;
vector<int> chess(6);
vector<int> input(6);

int main(int argc, char** argv) {
	chess[0] =1;
	chess[1] =1;
	chess[2] =2;
	chess[3] =2;
	chess[4] =2;
	chess[5] =8;
	for(int i =0; i<6; i++){
		cin>>input[i];
	}
	for(int i =0; i<6; i++){
		cout<< chess[i]-input[i]<<' ';
	}
	return 0;
}

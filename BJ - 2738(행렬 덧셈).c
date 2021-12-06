#include <stdio.h>

int main(){
  int n ,m;
  scanf("%d %d", &n, &m);
  int arrA[n][m] ;
  int ans[n][m] ;
  for(int i =0; i <n; i ++){
    for(int j =0;  j<m; j ++){
      scanf("%d", &arrA[i][j]);
    }
  }
  for(int i =0; i <n; i ++){
    for(int j =0;  j<m; j ++){
      scanf("%d", &ans[i][j]);
      ans[i][j] += arrA[i][j];
      printf("%d ", ans[i][j]);
    }
    printf("\n");
  }
}

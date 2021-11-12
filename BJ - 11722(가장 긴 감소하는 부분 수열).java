import java.lang.*;
import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		int [] arr = new int [1001];
		int [] dp = new int [1001];
		StringTokenizer st = new StringTokenizer(br.readLine());
		int max_cnt = 0; 
		for(int i = 0; i < N; i ++) {
			arr[i] = Integer.parseInt(st.nextToken());
			for(int j = 0; j <i; j ++) {
				if(arr[i] < arr[j]) {
					dp[i] = Math.max(dp[j] + 1, dp[i]);
					max_cnt = Math.max(max_cnt,dp[i]);
				}
			}
		}
		bw.write(max_cnt + 1 + "\n");
		
		bw.flush();
		bw.close();
		br.close();
 
    }
}

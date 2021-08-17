import java.lang.*;
import java.util.stream.IntStream;
import java.io.*;
import java.util.*;
import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws Exception { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int testcase = Integer.parseInt(br.readLine());
		for(int tmp =0; tmp < testcase; tmp ++) {
			String str[];
			int N = Integer.parseInt(br.readLine());
			int arr[][] = new int[N][2];
            int dp[][] = new int[N][2];
            for (int i = 0; i < 2; i++) {
                str = br.readLine().split(" ");
                for (int j = 0; j < N; j++) {
                    arr[j][i] = Integer.parseInt(str[j]);
                }
            }
            dp[0][0] = arr[0][0];
            dp[0][1] = arr[0][1];
			if (N != 1) {
	            dp[1][0] = dp[0][1] + arr[1][0];
	            dp[1][1] = dp[0][0] + arr[1][1];
	            for (int j = 2; j < N; j++) {
	            	dp[j][0] = Math.max(dp[j - 2][1],dp[j - 1][1]) + arr[j][0];
	                dp[j][1] = Math.max(dp[j - 2][0],dp[j - 1][0]) + arr[j][1];
	            }
			}
            bw.write(String.valueOf(Math.max(dp[N-1][0], dp[N-1][1]))+"\n");
		}
	
        bw.flush();
        br.close();
        bw.close();
 
    }
}
//
//¿¹½Ã
//4
//1
//50
//20
//2
//50 40 
//40 50
//4
//50 40 19 18
//40 20 40 20
//4
//40 40 39 40
//40 40 40 40

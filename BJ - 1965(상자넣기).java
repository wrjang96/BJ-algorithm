import java.util.*; 
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int array[] = new int[N+1];
		int dp[] = new int[N+1];
		int max = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			array[i] = Integer.parseInt(st.nextToken());
		}

		
		for (int i = 0; i <= N; i++) {
			dp[i] = 1;
			for (int j = 0; j <= i; j++) {
				if (array[j] < array[i])
					dp[i] = Math.max(dp[i], dp[j] + 1);
			}
			max = Math.max(max, dp[i]);
		}

		System.out.println(max);
	}
}

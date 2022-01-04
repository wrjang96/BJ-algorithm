	import java.util.*;
	import java.io.*;
	
	public class Main {
		static int sx,sy,ex,ey,N,M,K,ans;
		static int arr[][],sum_arr[][];
		public static void main(String[] args) throws IOException{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			StringTokenizer st;
			st = new StringTokenizer(br.readLine());
			N= Integer.parseInt(st.nextToken());
			M= Integer.parseInt(st.nextToken());
			arr = new int [N][M];
			sum_arr = new int [N+1][M+1];
			
			for(int i =0; i <N; i ++) {
				st = new StringTokenizer(br.readLine());
				for(int j =0; j <M; j ++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
					sum_arr[i+1][j+1] = sum_arr[i][j+1] + sum_arr[i+1][j] - sum_arr[i][j] + arr[i][j];
				}
			}
		K = Integer.parseInt(br.readLine());
		for(int i =0; i <K; i ++) {
			ans = 0;
			st = new StringTokenizer(br.readLine());
			sx = Integer.parseInt(st.nextToken());
			sy = Integer.parseInt(st.nextToken());
			ex = Integer.parseInt(st.nextToken());
			ey = Integer.parseInt(st.nextToken());
			ans = sum_arr[ex][ey] -sum_arr[ex][sy-1] - sum_arr[sx-1][ey] + sum_arr[sx-1][sy-1];
			bw.write(ans + "\n");
		}
		bw.flush();
		br.close();
		bw.close();
	}
	}
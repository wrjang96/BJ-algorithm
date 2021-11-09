import java.lang.*;
import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws Exception { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int [][] arr = new int [51][2];
		int N = Integer.parseInt(br.readLine());
		for(int i = 0; i < N; i ++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		for (int i = 0; i < N; i ++) {
			int rank = 1;
			for(int j = 0; j <N; j ++) {
				if(i !=j) {
					if(arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
						rank+=1;
					}
				}
			}
			bw.write(rank+ " ");
		}
		bw.flush();
		bw.close();
		br.close();
 
    }
}

import java.io.*;
import java.util.*;

public class Main {
	static final int INF =  987654321;
	
    public static void main(String[] args) throws NumberFormatException,IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int[][] arr = new int[N + 1][N + 1];
        
        for(int i = 0; i <N; i ++) {
        	for(int j = 0; j <N; j ++) {
        		arr[i][j] = INF;
        		if(i==j) {
        			arr[i][j] = 0;
        		}
        	}
        }
        for(int i = 0; i <M; i ++) {
        	st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	int c = Integer.parseInt(st.nextToken());
        	arr[a-1][b-1] = Math.min(arr[a-1][b-1], c);
        }
        for(int k = 0; k <N; k++) {
        	for(int i = 0; i <N; i++) {
        		for(int j = 0; j <N; j++) {
        			if(arr[i][j] > arr[i][k] + arr[k][j]) {
        				arr[i][j] = arr[i][k] + arr[k][j];
        			}
        		}
        	}
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <N; i++) {
    		for(int j = 0; j <N; j++) {
    			if(arr[i][j] == INF) {
    				arr[i][j] = 0;
    			}
    			sb.append(arr[i][j] + " ");
    		}
    		sb.append("\n");
    	}
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

}
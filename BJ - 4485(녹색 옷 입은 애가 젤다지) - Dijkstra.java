import java.io.*;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static class point implements Comparable<point>{
		int x, y, cost;
		public point(int x, int y, int cost) {
			super();
			this.x = x;
			this.y = y;
			this.cost = cost;
		}
		@Override
		public int compareTo(point O) {
			return this.cost- O.cost;
		}
	}
	public static int dijkstra() {
		PriorityQueue<point> pq = new PriorityQueue<point>();
		sum_cnt[0][0] = graph[0][0];
		pq.offer(new point(0,0,graph[0][0]));
		while(!pq.isEmpty()) {
			point temp = pq.poll();
			for(int i = 0; i <4; i ++) {
				int nx = temp.x + dx[i];
				int ny = temp.y + dy[i];
				if(0<= nx && nx <N && 0<= ny && ny<N) { 
					if (sum_cnt[nx][ny] > sum_cnt[temp.x][temp.y] + graph[nx][ny]) {
						sum_cnt[nx][ny] = sum_cnt[temp.x][temp.y] + graph[nx][ny];
						pq.offer(new point(nx,ny,graph[nx][ny]));
					}
				}
				
			}
		}
		return sum_cnt[N-1][N-1];
	}
	static int N;
	static int[][] graph;
	static int [][] sum_cnt;
	static int dx[] = {-1,1,0,0};
	static int dy[] = {0,0,1,-1};
	
	
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));  
        StringTokenizer st = null; 
        StringBuilder sb = new StringBuilder();
        int cnt = 1;
        while(true) {
        	N = Integer.parseInt(br.readLine());
        	if(N==0) {
        		break;
        	}
        	graph = new int [N+1][N+1];
        	sum_cnt = new int[N+1][N+1];
        	for(int i = 0; i <N; i ++) {
        		st = new StringTokenizer(br.readLine());
        		for(int j = 0; j <N; j ++) {
        			graph[i][j] = Integer.parseInt(st.nextToken());
        			sum_cnt[i][j] = Integer.MAX_VALUE;
        		}
        	}
        	sb.append("Problem " + cnt + ": " + dijkstra() + "\n"); 
        	cnt +=1;
        }
//        bw.write(sb.toString());
        System.out.println(sb); 
        br.close();
    }
}
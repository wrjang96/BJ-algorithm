import java.lang.*;
import java.math.BigInteger;
import java.io.*;
import java.util.*;
import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws Exception { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
		StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
 
        BigInteger a = BigInteger.ONE;
        BigInteger b = BigInteger.ONE;
        // 숫자 1을 나타내는 값을 가져옴
        int start = 1;
        int end = N;
        for(int i = 0; i < M; i++){
            a = a.multiply(new BigInteger(String.valueOf(end--)));
            b = b.multiply(new BigInteger(String.valueOf(start++)));
            // 큰 숫자의 연산을 할 때 자바에서는 BigInteger를 사용한다.
            // BigInteger는 문자열을 입력 값으로 가져야 한다. 
        }
        BigInteger ans = a.divide(b);
        bw.write(ans + "\n");

        bw.flush();
        br.close();
        bw.close();
 
    }
}

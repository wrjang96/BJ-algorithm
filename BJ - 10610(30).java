import java.util.*;
import java.io.*;

public class Main{
    static int[] Arr;
    static int strLen;
	public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String inputString = br.readLine();
        int sum = 0;
        
        strLen = inputString.length();
        Arr = new int[10];
        long total = 0;
        
        for(int i =0; i <strLen; i ++) {
        	int temp = Integer.parseInt(inputString.substring(i,i+1));
        	Arr[temp] +=1;
        	total +=temp;
        }
        
        if(inputString.contains("0")&& total %3 ==0) {
        	for(int i = 9; i >=0; i --) {
        		while(Arr[i]>0) {
        			System.out.print(i);
        			Arr[i]--;
        		}
        	}
        }
        else {
        	System.out.println(-1);
        }
}
}
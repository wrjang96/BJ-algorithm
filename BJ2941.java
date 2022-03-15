import java.io.*;
import java.util.*;

public class BJ2941 {
    public void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] cro_alphabet = {"c=","c-","dz=","d-","lj","nj","s=","z="};
        String temp = br.readLine().trim();

        int answer = 0;
        for(int i =0; i< cro_alphabet.length; i++){
            if (temp.contains(cro_alphabet[i])){
                temp = temp.replaceAll(cro_alphabet[i], "A");
            }
        }
        answer = temp.length();
        bw.write(answer + " ");
        bw.flush();
        br.close();bw.close();
    }
}

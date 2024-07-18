import java.util.*;
import java.lang.*;
import java.io.*;
// 2024-01-09
// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int Cnt = Integer.parseInt(br.readLine());
        int num[] = new int[6];

        for(int i=0;i<Cnt;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int j=0;j<6;j++){
                num[j] = Integer.parseInt(st.nextToken());
            }

            double PtP_distance= Math.sqrt(Math.pow(num[0] - num[3], 2) + Math.pow(num[1] - num[4], 2));

            if((num[2] == num[5] &&  PtP_distance == 0)){
                System.out.println(-1);
            }
            else if(PtP_distance == num[2]+ num[5] || PtP_distance == Math.abs(num[2] - num[5]) ){
                System.out.println(1);
            }
            else if(PtP_distance < num[2]+ num[5] && PtP_distance > Math.abs(num[2] - num[5]) ){
                System.out.println(2);
            }
            else{
                System.out.println(0);
            }
        }
    }
}



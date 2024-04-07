import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언

        int n = Integer.parseInt(bf.readLine());
        String[] arr = new String[n];
        for(int i = 0; i < n; i++) {
            arr[i] = bf.readLine();
        }

        for (int i = 0; i < arr[0].length(); i++) {
            int count = 0;
            for(int j = 0; j < (n - 1); j++) {
                if(arr[j].charAt(i) != arr[j + 1].charAt(i)) {
                    break;
                }
                count++;
            }
            if(count == (n - 1)) {
                System.out.print(arr[0].charAt(i));
            }else {
                System.out.print("?");
            }
        }
    }
}
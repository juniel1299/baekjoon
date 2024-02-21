import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        //0.001 ~ 100.000
        //1~ 100000
        int[] answer = new int[100001];
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            answer[(int) (Double.parseDouble(br.readLine()) * 1000)]++;
        }

        for (int i = 0; i < answer.length; i++) {
            while (answer[i] > 0 && cnt < 7) {
                System.out.printf("%.3f\n", i / 1000.0);
                answer[i]--;
                cnt++;
            }
        }
    }
}
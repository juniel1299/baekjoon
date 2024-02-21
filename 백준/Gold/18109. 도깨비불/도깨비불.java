import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        
        Set<Character> ja = new HashSet<>(Arrays.asList('q', 'w', 'e', 'r', 'R', 't', 'T',
                                                        'a', 's', 'd', 'f', 'g',
                                                        'z', 'x', 'c', 'v'));
        Set<Character> mo = new HashSet<>(Arrays.asList('y', 'u', 'i', 'o', 'O', 'p', 'P',
                                                        'h', 'j', 'k', 'l',
                                                        'b', 'n', 'm'));
        Set<String> ssang = new HashSet<>(Arrays.asList("rt", "sw", "sg", "fr", "fa",
                                                        "fq", "ft", "fx", "fv", "fg", "qt"));

        int sLen = s.length();
        int answer = 0;
        for (int i = 1; i < sLen - 2; i++) {
            if (mo.contains(s.charAt(i - 1)) && ja.contains(s.charAt(i)) && mo.contains(s.charAt(i + 1))) {
                answer += 1;
            }
            if (mo.contains(s.charAt(i - 1)) && ssang.contains(s.substring(i, i + 2)) && mo.contains(s.charAt(i + 2))) {
                answer += 1;
            }
        }

        if (mo.contains(s.charAt(sLen - 3)) && ja.contains(s.charAt(sLen - 2)) && mo.contains(s.charAt(sLen - 1))) {
            answer += 1;
        }
        System.out.println(answer);
    }
}

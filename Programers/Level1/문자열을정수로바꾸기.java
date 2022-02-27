package Programers.Level1;

public class 문자열을정수로바꾸기 {
    public int solution(String s) {
        if(!s.startsWith("-"))
            return Integer.parseInt(s);
        else{
            String tmp = s.substring(1,s.length());
            return -Integer.parseInt(tmp);
        }
        
    }
}

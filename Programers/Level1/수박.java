package Programers.Level1;

public class 수박 {
    char[] ch = {'수','박'};                                                                          
    public String solution(int n) {
        String answer = "";
        
        for(int i=0; i < n; i++){
            answer += ch[i%2];
        }
        
        return answer;
    }
}

package Programers.Level1;

public class 이상한문자만들기 {

    public String solution(String s) {
        String answer = "";
        int cnt = 2;
        for(int i=0; i < s.length(); i++){
            String ss = s.charAt(i)+"";
            if(s.charAt(i) == ' '){
                cnt = 2;
                answer += " ";
                continue;              
            }
            
            else if(cnt % 2 == 0)
                answer += ss.toUpperCase();
            else
                answer += ss.toLowerCase();
            
            cnt++;            
        }        
        return answer;
    }

}

package Programers.Level1;

class 핸드폰번호가리기 {
    public StringBuilder solution(String phone_number) {
        StringBuilder answer = new StringBuilder();
        String str = phone_number.substring(phone_number.length()-4,phone_number.length());
        System.out.print(str);
        for(int i=0; i < phone_number.length()-4; i++){
            answer.append("*");
        }
        answer.append(str);
        return answer;
    }
}
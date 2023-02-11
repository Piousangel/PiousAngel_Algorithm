function chkNum(num) {
    if (0 <= num && num <= 9) {
        return true;
    }
    return false;
}
function solution(my_string) {
    let answer = 0;
    let temp = "";

    for (ch of my_string) {
        if (chkNum(Number(ch))) {
            temp += ch;
        } else {
            answer += Number(temp);
            temp = "";
        }
    }
    answer += Number(temp);
    return answer;
}

function chkNum(num) {
    if (1 <= num && num <= 9) {
        return true;
    }
    return false;
}
function solution(my_string) {
    let answer = 0;
    let temp = "";

    for (ch of my_string) {
        if (chkNum(Number(ch))) {
            console.log();
            answer += Number(ch);
        }
    }
    return answer;
}

function solution(cards1, cards2, goal) {
    let answer = "";
    let flag = true;

    for (str of goal) {
        if (cards1[0] === str) {
            cards1.shift();
        } else if (cards2[0] === str) {
            cards2.shift();
        } else {
            answer = "No";
            flag = false;
            break;
        }
    }
    if (flag) {
        answer = "Yes";
    }

    return answer;
}

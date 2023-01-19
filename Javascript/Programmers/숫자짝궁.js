function solution(X, Y) {
    let answer = "";

    let temp = [];
    let XArr = Array.from(X);
    let YArr = Array.from(Y);

    for (let i = 0; i < XArr.length; i++) {
        for (let j = 0; j < YArr.length; j++) {
            if (XArr[i] === YArr[j]) {
                temp.push(XArr[i]);
                YArr.splice(j, 1);
                break;
            }
        }
    }
    if (temp.length === 0) {
        return "-1";
    }
    answer = temp.sort((a, b) => b - a).join("");

    answer = Number(answer) === 0 ? "0" : answer;
    return answer;
}

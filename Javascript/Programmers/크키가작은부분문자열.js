function solution(t, p) {
    let answer = 0;

    let pLen = p.length;

    for (let i = 0; i < t.length - pLen + 1; i++) {
        let temp = "";
        for (let j = 0; j < pLen; j++) {
            temp += t[i + j];
        }
        if (Number(temp) <= Number(p)) answer += 1;
    }

    return answer;
}

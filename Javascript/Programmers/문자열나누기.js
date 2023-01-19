function solution(s) {
    let answer = 0;
    let startIdx = 0;
    let idx = 0;
    let temp = "";
    let cnt1 = 0;
    let cnt2 = 0;

    while (idx < s.length) {
        if (cnt1 === cnt2) {
            cnt1 = 0;
            cnt2 = 0;
            temp = "";
            answer += 1;
        }
        if (temp === "") {
            cnt1 += 1;
            temp = s[idx];
            idx += 1;
        } else {
            if (temp === s[idx]) {
                cnt1 += 1;
                idx += 1;
            } else {
                cnt2 += 1;
                idx += 1;
            }
        }
    }

    return answer;
}

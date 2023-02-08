function solution(common) {
    let answer = 0;
    const last = common[common.length - 1];
    // 등차
    if (common[2] - common[1] === common[1] - common[0]) {
        answer = last + common[2] - common[1];
    }
    //등비
    else {
        answer = last * (common[2] / common[1]);
    }

    return answer;
}

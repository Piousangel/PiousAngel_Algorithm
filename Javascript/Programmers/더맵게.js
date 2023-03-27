function solution(heights) {
    let answer = [];
    let len = heights.length;
    let idx = 0;

    for (let i = len - 1; i > 0; i--) {
        let compare = heights[i];
        let subArr = heights.slice(0, i);
        let temp = subArr.reverse().find((num) => num > compare);

        if (temp !== undefined) {
            subArr.reverse().map((num, i) => {
                if (num === temp) {
                    idx = i + 1;
                }
            });
        } else {
            idx = 0;
        }
        answer.unshift(idx);
    }

    answer.unshift(0);
    return answer;
}


// git 서버가 이상한가?
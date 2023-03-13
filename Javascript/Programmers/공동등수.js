// N명의 학생의 시험 점수를 바탕 등수 부여
// 세 학생이 있고 동점이면 공동 그 등수, 그리고 다음등수는 - 공동등수만큼

function solution(grade) {
    let answer = [];

    const map = new Map();

    for (let i = 1; i <= grade.length; i++) {
        map.set(i, grade[i - 1]);
    }

    const sortedMap = new Map(
        [...map]
            .sort((a, b) => {
                if (a[1] === b[1]) {
                    return b[0] - a[0];
                } else {
                    return a[1] - b[1];
                }
            })
            .reverse()
    );

    const maxVal = grade.sort()[grade.length - 1];
    const rankMap = new Map();
    let rank = 1;
    let cnt = 0;
    let score = maxVal;
    let tempArr = [];
    for (const items of sortedMap) {
        if (score === items[1]) {
            tempArr.push(items[0]);
            cnt += 1;
        } else {
            score = items[1];
            if (tempArr.length > 0) {
                for (const num of tempArr) {
                    rankMap.set(num, rank);
                }
            }
            tempArr = [items[0]];
            rank += cnt;
            cnt = 1;
        }
    }

    if (tempArr.length > 0) {
        for (const num of tempArr) {
            rankMap.set(num, rank);
        }
    }

    const resultMap = new Map([...rankMap].sort((a, b) => a[0] - b[0]));

    for (const items of resultMap) {
        answer.push(items[1]);
    }

    return answer;
}

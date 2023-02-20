function solution(lines) {
    let answer = 0;

    const map = new Map();

    const sortedLines = lines.sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        }
        return a[0] - b[0];
    });

    for (const line of lines) {
        const start = line[0];
        const end = line[1];

        for (let i = start; i <= end; i++) {
            map.set(i, (map.get(i) || 0) + 1);
        }
    }

    let len = -1;
    let flag = false;
    for (const [key, value] of map) {
        if (value > 1) {
            flag = true;
            len += 1;
        } else {
            if (flag) {
                answer += len;
                flag = false;
                len = -1;
            }
        }
    }
    if (flag) answer += len;
    return answer;
}

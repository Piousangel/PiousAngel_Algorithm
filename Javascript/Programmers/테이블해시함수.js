function solution(data, col, row_begin, row_end) {
    let answer = 0;

    const sortedData = data.sort((a, b) => {
        if (a[col - 1] === b[col - 1]) {
            return b[0] - a[0];
        }
        return a[col - 1] - b[col - 1];
    });

    for (let i = row_begin; i <= row_end; i++) {
        answer ^= sortedData[i - 1]
            .map((v) => v % i)
            .reduce((a, b) => a + b, 0);
    }

    return answer;
}

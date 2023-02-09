function solution(num, total) {
    let temp = parseInt(total / num);
    let startIdx = parseInt((num - 1) / 2);

    let idx = 0;
    const arr = new Array(num).fill(temp - startIdx).map((e) => {
        return e + idx++;
    });

    return arr;
}

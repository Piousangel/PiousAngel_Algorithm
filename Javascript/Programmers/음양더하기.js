function solution(absolutes, signs) {

    const result = absolutes.reduce((acc, cur, idx) => {
        cur = signs[idx] === true ? absolutes[idx] : -absolutes[idx];
        return (acc += cur);
    }, 0);

    return result;
}

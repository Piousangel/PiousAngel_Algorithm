function solution(order) {
    return [...String(order)].filter(
        (n) => Number(n) % 3 === 0 && Number(n) !== 0
    ).length;
}

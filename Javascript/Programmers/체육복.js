function solution(n, lost, reserve) {
    let answer = 0;

    const temptempLost = lost
        .sort((a, b) => a - b)
        .filter((lost) => !reserve.includes(lost));
    let hasReserve = reserve
        .sort((a, b) => a - b)
        .filter((reverse) => !lost.includes(reverse));

    const result = temptempLost.filter((lost) => {
        const lendValue = hasReserve.find(
            (reserve) => Math.abs(reserve - lost) == 1
        );
        if (!lendValue) {
            return lost;
        }

        hasReserve = hasReserve.filter((reverse) => reverse !== lend);
    });

    answer = n - result.length;

    return answer;
}

function solution(dots) {
    const x1 = dots[0][0];
    const y1 = dots[0][1];
    const x2 = dots[1][0];
    const y2 = dots[1][1];
    const x3 = dots[2][0];
    const y3 = dots[2][1];
    const x4 = dots[3][0];
    const y4 = dots[3][1];

    if (
        Math.abs(x1 - x2) === Math.abs(x3 - x4) &&
        Math.abs(y1 - y2) === Math.abs(y3 - y4)
    ) {
        return 1;
    }
    if (
        Math.abs(x1 - x3) === Math.abs(x2 - x4) &&
        Math.abs(y1 - y3) === Math.abs(y2 - y4)
    ) {
        return 1;
    }
    if (
        Math.abs(x1 - x4) === Math.abs(x2 - x3) &&
        Math.abs(y1 - y4) === Math.abs(y2 - y3)
    ) {
        return 1;
    }

    return 0;
}

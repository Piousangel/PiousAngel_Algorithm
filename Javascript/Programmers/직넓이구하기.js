function solution(dots) {
    const row =
        Math.max(...dots.map((d) => d[0])) - Math.min(...dots.map((d) => d[0]));
    const col =
        Math.max(...dots.map((d) => d[1])) - Math.min(...dots.map((d) => d[1]));
    return row * col;
}

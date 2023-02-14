function solution(edges) {
    const rowLength = edges.length;
    const colLength = edges[0].length;
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];

    let answer = 0;
    let visitedCahce = Array.from(Array(rowLength), () =>
        new Array(colLength).fill(0)
    );
    let q = [];

    for (let rowIdx = 0; rowIdx < rowLength; rowIdx++) {
        for (let colIdx = 0; colIdx < colLength; colIdx++) {
            // 최초 캐시된 엣지들
            if (
                edges[rowIdx][colIdx] === 1 &&
                visitedCahce[rowIdx][colIdx] === 0
            ) {
                q.push([rowIdx, colIdx]);

                while (q.length > 0) {
                    const [y, x] = q.shift();

                    for (let dir = 0; dir < 4; dir++) {
                        const nx = x + dx[dir];
                        const ny = y + dy[dir];

                        if (
                            0 <= nx &&
                            nx < colLength &&
                            0 <= ny &&
                            ny < rowLength &&
                            edges[ny][nx] === 0
                        ) {
                            // 전파되지 않았거나 더 짧게 전파 될 수 있는 경우
                            if (
                                visitedCahce[ny][nx] === 0 ||
                                visitedCahce[ny][nx] > visitedCahce[y][x] + 1
                            ) {
                                visitedCahce[ny][nx] = visitedCahce[y][x] + 1;
                                q.push([ny, nx]);
                            }
                        }
                    }
                }
            }
        }
    }

    answer = Math.max(...visitedCahce.flat());
    return answer;
}

// const edges = [
//     [0, 1],
//     [1, 0],
// ];

const edges = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
];

console.log(solution(edges));

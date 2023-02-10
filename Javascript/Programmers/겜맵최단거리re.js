function solution(maps) {
    let answer = 0;
    const row = maps.length;
    const col = maps[0].length;

    let visited = Array.from(Array(row), () => new Array(col).fill(-1));
    visited[0][0] = 1;

    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];

    let q = [];
    q.push([0, 0]);

    while (q.length > 0) {
        const [y, x] = q.shift();

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (0 <= nx && nx < col && 0 <= ny && ny < row) {
                if (maps[ny][nx] === 1 && visited[ny][nx] === -1) {
                    visited[ny][nx] = visited[y][x] + 1;
                    q.push([ny, nx]);
                }
            }
        }
    }

    answer = visited[row - 1][col - 1];
    return answer;
}

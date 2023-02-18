// s : 시작 , e 출구 , l 레버, o 통로, x 레버

function bfs(start, end, maps) {
    const row = maps.length;
    const col = maps[0].length;
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];

    let q = [];
    let visited = Array.from(Array(row), () => new Array(col).fill(false));

    visited[start[0]][start[1]] = true;

    q.push([...start, 0]);

    while (q.length > 0) {
        const [y, x, cnt] = q.shift();

        if (y === end[0] && x === end[1]) {
            return cnt;
        }

        for (let idx = 0; idx < 4; idx++) {
            const nx = x + dx[idx];
            const ny = y + dy[idx];

            if (
                0 <= nx &&
                nx < col &&
                0 <= ny &&
                ny < row &&
                maps[ny][nx] !== "X" &&
                visited[ny][nx] === false
            ) {
                visited[ny][nx] = true;
                q.push([ny, nx, cnt + 1]);
            }
        }
    }
    return -100;
}

function solution(maps) {
    let start = [0, 0];
    let lever = [0, 0];
    let end = [0, 0];

    for (let i = 0; i < maps.length; i++) {
        for (let j = 0; j < maps[0].length; j++) {
            if (maps[i][j] === "S") {
                start[0] = i;
                start[1] = j;
            }
            if (maps[i][j] === "E") {
                end[0] = i;
                end[1] = j;
            }
            if (maps[i][j] === "L") {
                lever[0] = i;
                lever[1] = j;
            }
        }
    }

    let StoL = bfs(start, lever, maps);
    let LtoE = bfs(lever, end, maps);

    return StoL + LtoE < 0 ? -1 : StoL + LtoE;
}

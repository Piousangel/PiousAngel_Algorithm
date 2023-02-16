// s : 시작 , e 출구 , l 레버, o 통로, x 레버
function solution(maps) {
    let result = 100000;
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    const row = maps.length;
    const col = maps[0].length;

    // let visited = Array.from(Array(row), () => new Array(col).fill(0));
    let flag = false;
    let q = [];

    for (let i = 0; i < row; i++) {
        if (flag) break;
        for (let j = 0; j < col; j++) {
            if (maps[i][j] === "S") {
                flag = true;
                q.push([i, j, 0, false]);
                while (q.length > 0) {
                    const [y, x, cnt, lever] = q.shift();

                    if (lever && maps[y][x] === "E") {
                        result = Math.min(result, cnt);
                        break;
                    }
                    if (cnt > result) {
                        break;
                    }

                    for (let idx = 0; idx < 4; idx++) {
                        const nx = x + dx[idx];
                        const ny = y + dy[idx];

                        if (
                            0 <= nx &&
                            nx < col &&
                            0 <= ny &&
                            ny < row &&
                            maps[ny][nx] !== "X"
                        ) {
                            if (maps[ny][nx] === "L") {
                                q.push([ny, nx, cnt + 1, true]);
                            } else q.push([ny, nx, cnt + 1, lever]);
                        }
                    }
                }
            }
        }
    }
    if (result !== 100000) return result;
    else return -1;
}


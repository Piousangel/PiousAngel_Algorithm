function solution(maps) {
    let answer = [];
    let value_list = [];
    let map = [];

    for (let i = 0; i < maps.length; i++) {
        map.push([...maps[i]]);
    }
    const row = map.length;
    const col = map[0].length;
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];

    let visited = Array.from(Array(row), () => new Array(col).fill(0));

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (map[i][j] !== "X" && visited[i][j] === 0) {
                let q = [];
                let temp = 0;
                q.push([i, j]);
                visited[i][j] = 1;

                while (q.length > 0) {
                    const [y, x] = q.shift();
                    temp += Number(map[y][x]);

                    for (let k = 0; k < 4; k++) {
                        const nx = x + dx[k];
                        const ny = y + dy[k];

                        if (0 <= nx && nx < col && 0 <= ny && ny < row) {
                            if (visited[ny][nx] === 0 && map[ny][nx] !== "X") {
                                visited[ny][nx] = 1;
                                q.push([ny, nx]);
                            }
                        }
                    }
                }
                value_list.push(temp);
            }
        }
    }

    if (value_list.length === 0) {
        return [-1];
    }
    answer = value_list.sort((a, b) => {
        return a - b;
    });
    return answer;
}

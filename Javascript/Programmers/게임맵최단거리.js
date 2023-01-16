function solution(maps) {
    let answer = 1;

    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];
    const row = maps.length;
    const col = maps[0].length;
    let q = [];
    let visited = maps;

    visited[0][0] = 0;
    q.push([0, 0]);

    while (q.length > 0) {
        let qLen = q.length;
        for (let i = 0; i < qLen; i++) {
            let [y, x] = q.shift();

            for (let j = 0; j < 4; j++) {
                let nx = x + dx[j];
                let ny = y + dy[j];

                if (
                    0 <= nx &&
                    nx < col &&
                    0 <= ny &&
                    ny < row &&
                    visited[ny][nx] === 1
                ) {
                    if (nx === col - 1 && ny === row - 1) {
                        return ++answer;
                    }
                    q.push([ny, nx]);
                    visited[ny][nx] = 0;
                }
            }
        }
        
        answer++;
    }
    return -1;
}

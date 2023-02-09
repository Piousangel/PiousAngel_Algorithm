function solution(board) {
    let answer = 0;

    const dx = [-1, 0, 1, 1, 1, 0, -1, -1];
    const dy = [1, 1, 1, 0, -1, -1, -1, 0];

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] === 1) {
                for (let k = 0; k < 8; k++) {
                    let nx = i + dx[k];
                    let ny = j + dy[k];

                    if (
                        0 <= nx &&
                        nx < board.length &&
                        0 <= ny &&
                        ny < board[0].length
                    ) {
                        if (board[nx][ny] !== 1) {
                            board[nx][ny] = 2;
                        }
                    }
                }
            }
        }
    }

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] === 0) {
                answer += 1;
            }
        }
    }

    return answer;
}

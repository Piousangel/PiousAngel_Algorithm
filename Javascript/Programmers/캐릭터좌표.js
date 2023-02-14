function solution(keyinput, board) {
    const map = new Map();

    let nx = 0;
    let ny = 0;
    let smallRow = -(board[1] - 1) / 2;
    let bigRow = (board[1] - 1) / 2;
    let smallCol = -(board[0] - 1) / 2;
    let bigCol = (board[0] - 1) / 2;

    map.set("left", [-1, 0]);
    map.set("right", [1, 0]);
    map.set("up", [0, 1]);
    map.set("down", [0, -1]);

    for (input of keyinput) {
        const [x, y] = map.get(input);
        if (
            smallCol <= nx + x &&
            nx + x <= bigCol &&
            smallRow <= ny + y &&
            ny + y <= bigRow
        ) {
            nx += x;
            ny += y;
        }
    }

    return [nx, ny];
}

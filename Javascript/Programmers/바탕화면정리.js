function solution(wallpaper) {
    const xArr = [];
    const yArr = [];
    const row = wallpaper.length;
    const col = wallpaper[0].length;

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (wallpaper[i][j] === "#") {
                yArr.push(i);
                xArr.push(j);
            }
        }
    }

    xArr.sort((a, b) => a - b);
    yArr.sort((a, b) => a - b);

    return [
        yArr[0],
        xArr[0],
        yArr[yArr.length - 1] + 1,
        xArr[xArr.length - 1] + 1,
    ];
}

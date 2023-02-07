function solution(book_time) {
    let answer = 0;

    let intArr = [];

    for (let i = 0; i < book_time.length; i++) {
        let tempSum = 0;
        let tempArr = [];
        for (let j = 0; j < book_time[0].length; j++) {
            let timeArr = book_time[i][j].split(":");

            tempSum = Number(timeArr[0]) * 60 + Number(timeArr[1]);
            tempArr.push(tempSum);
        }

        intArr.push(tempArr);
    }

    intArr.sort((a, b) => a[0] + a[1] - (b[0] + b[1]));
    console.log(intArr);

    return answer;
}

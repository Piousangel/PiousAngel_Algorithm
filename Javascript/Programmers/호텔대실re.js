function converterT(time) {
    const [hour, min] = time.split(":");

    return parseInt(hour) * 60 + parseInt(min);
}

function solution(book_time) {
    let answer = 0;
    let cnt = 0;
    let arr = [];

    for (time of book_time) {
        const startTime = converterT(time[0]);
        const endTime = converterT(time[1]) + 10;

        arr.push([startTime, "start"]);
        arr.push([endTime, "end"]);
    }

    const sortedArr = arr.sort((a, b) => {
        if (a[0] === b[0]) {
            return b[1] - a[1];
        }
        return a[0] - b[0];
    });

    for (const [time, type] of sortedArr) {
        if (type === "start") {
            cnt += 1;
        } else {
            cnt -= 1;
        }
        answer = Math.max(answer, cnt);
    }

    return answer;
}

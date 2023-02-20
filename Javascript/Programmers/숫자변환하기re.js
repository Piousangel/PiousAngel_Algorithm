function solution(x, y, n) {
    let answer = -100;
    const set = new Set();

    q = [];
    q.push([x, 0]);

    while (q.length > 0) {
        const size = q.length;
        for (let i = 0; i < size; i++) {
            if (q[0][0] === y) {
                return q[0][1];
            }

            const [total, cnt] = q.shift();

            if (total * 3 <= y && !set.has(total * 3)) {
                set.add(total * 3);
                q.push([total * 3, cnt + 1]);
            }
            if (total * 2 <= y && !set.has(total * 2)) {
                set.add(total * 2);
                q.push([total * 2, cnt + 1]);
            }
            if (total + n <= y && !set.has(total + n)) {
                set.add(total + n);
                q.push([total + n, cnt + 1]);
            }
        }
    }

    return -1;
}

// function solution(x, y, n) {

//     let cnt = 0;
//     const set = new Set();

//     q = [];
//     q.push(x);

//     while(q.length > 0){
//         const size = q.length;
//         for(let i=0 ; i < size; i++) {
//             if(q[0] === y) {
//                 return cnt;
//             }

//             checkTotal(q.shift(), y, n, set, q);
//         }
//         cnt +=1;
//     }

//     return -1;
// }

// function checkTotal(total, y, n, set, q){

//     if(total * 3 <= y && !set.has(total * 3)){
//         set.add(total * 3);
//         q.push(total * 3);
//     }
//     if(total * 2 <= y && !set.has(total * 2)){
//         set.add(total * 2);
//         q.push(total * 2);
//     }
//     if(total + n <= y && !set.has(total + n)){
//         set.add(total + n);
//         q.push(total + n);
//     }
//     return;
// }

function solution(x, y, n) {
    if (x === y) {
        return 0;
    }
    const searchedArr = { x: true };
    let q = [];
    let cnt = 0;
    q.push(x);

    while (queue.length !== 0) {
        const size = queue.length;
        cnt += 1;
        const nQ = [];

        for (let i = 0; i < size; i++) {
            const num = queue.pop();
            for (const next of [num + n, num * 2, num * 3]) {
                if (next === y) {
                    return cnt;
                }
                if (next > y) {
                    continue;
                }
                if (!searchedArr[next]) {
                    searchedArr[next] = true;
                    nQ.push(next);
                }
            }
        }
        q = nQ;
    }
    return -1;
}

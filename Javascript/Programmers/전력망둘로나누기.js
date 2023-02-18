function solution(n, wires) {
    let minValue = 10001;

    for (let i = 0; i < wires.length; i++) {
        const leftWire = chkWire(wires, i);
        const rightWire = n - leftWire;
        const temp = Math.abs(leftWire - rightWire);
        minValue = Math.min(minValue, temp);
    }

    return minValue;
}

function chkWire(wires, idx) {
    let cnt = 0;
    const w_list = [...wires];

    q = [];
    q.push(w_list[idx][1]);
    w_list.splice(idx, 1);

    while (q.length > 0) {
        const k = q.shift();

        for (let i = 0; i < w_list.length; i++) {
            let flag = false;
            let temp = w_list[i];

            if (temp[0] === k) {
                q.push(temp[1]);
                // w_list.filter(v => v !== temp);
                for (let i = 0; i < w_list.length; i++) {
                    if (w_list[i] === temp) {
                        w_list.splice(i, 1);
                        i--;
                    }
                }
                flag = true;
            } else if (temp[1] === k) {
                q.push(temp[0]);
                // w_list.filter(v => v !== temp);
                for (let i = 0; i < w_list.length; i++) {
                    if (w_list[i] === temp) {
                        w_list.splice(i, 1);
                        i--;
                    }
                }
                flag = true;
            }

            if (flag) {
                i -= 1;
            }
        }
        cnt += 1;
    }
    return cnt;
}

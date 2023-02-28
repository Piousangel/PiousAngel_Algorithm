function solution() {
    //2~5
    arr1 = new Array(4).fill(0).map((v, idx) => {
        return idx + 2;
    });

    //6~9
    arr2 = [...arr1].map((v, idx) => {
        return v + 4;
    });
    printGUGUDAN(arr1);
    console.log();
    printGUGUDAN(arr2);
}

function printGUGUDAN(arr) {
    for (let i = 1; i <= 9; i++) {
        if (i % 4 !== 0) {
            for (const num of arr) {
                let space = "    ";
                if (String(num * i).length === 1) {
                    space = "     ";
                }
                process.stdout.write(num + " * " + i + " = " + num * i + space);
            }
            console.log();
        }
    }
}

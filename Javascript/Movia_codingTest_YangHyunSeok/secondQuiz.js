const fs = require("fs");
let inputList = fs.readFileSync("./secondQuizInput.txt").toString();
inputList = inputList.split("\n");

//Nitin, Sobhagya 중 많은 코인을 가지고 있는 사람이 승리하는 문제입니다.
// 만약 코인이 같을 시, Nitin이 승리합니다.
// C코인은 current not winning 한테 전달하고, 그 이후, D코인도 current not winning 전달합니다. 이후 최종 승리자를 출력합니다.

function mainFunction() {
    const count = Number(inputList[0]);

    for (let index = 1; index <= count; index++) {
        const coinList = inputList[i].split(" ").map((value) => Number(value));

        //Nitin`s coin
        const A = coinList[0];
        // Sobhagya`s coin
        const B = coinList[1];
        // Ritik' coin in possession

        // giveList have Ritik' coin in possession && Satyarth' coin in possession (C, D)
        const giveList = coinList.filter((_, index) => {
            return index > 1;
        });

        console.log(getWinner(A, B, giveList));
    }
}

const getWinner = (A, B, giveList) => {
    let nitinCoin = A;
    let sobhagyaCoin = B;
    const count = giveList.length;

    for (let index = 0; index < count; index++) {
        if (nitinCoin >= sobhagyaCoin) {
            nitinCoin += giveList[index];
        } else {
            sobhagyaCoin += giveList[index];
        }
    }

    return nitinCoin >= sobhagyaCoin ? "N" : "S";
};

mainFunction();

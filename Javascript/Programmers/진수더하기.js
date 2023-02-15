function changeTenjinsu(str) {
    let result = 0;
    let idx = 0;

    for (let i = str.length - 1; i >= 0; i--) {
        let num = Number(str.charAt(i));
        if (num === 1) {
            result += 2 ** idx;
        }
        idx += 1;
    }
    return result;
} 

function solution(bin1, bin2) {
    return (changeTenjinsu(bin1) + changeTenjinsu(bin2)).toString(2);
}

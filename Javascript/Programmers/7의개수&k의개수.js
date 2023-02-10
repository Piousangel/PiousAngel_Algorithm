function solution(array) {
    let answer = 0;
    for (num of array) {
        const tempArr = [...String(num)];
        for (ch of tempArr) {
            if (ch === "7") answer += 1;
        }
    }
    return answer;
}

function solution(i, j, k) {
    let answer = 0; 
    for(let t = i; t <= j ; t++){
        const arr = [...String(t)];
        for(ch of arr){
            if(ch === String(k)){
                answer +=1;
            }
        }
    }
    return answer;
}

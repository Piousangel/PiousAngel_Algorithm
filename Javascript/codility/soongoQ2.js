
// Q2
function solution(N) {
    
    let tempArr = [];
    let tempSum = [];
    let Arr = Array.from(String(N));
    tempArr = [...Arr];

    for(let i = 0; i < Arr.length; i++){
        if(Arr[i] === '5'){
            let tempNum1 = tempArr.slice(0,i)
            let tempNum2 = tempArr.slice(i+1, Arr.length);
            let temp = [...tempNum1 , ...tempNum2];
            // console.log(temp)
            tempSum.push(Number(temp.join('')));
            
        }
    }
    const answer = Math.max(...tempSum);
    return answer;
}

// Q1
function solution(S, K) {

    const date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

    let tempIdx = date.indexOf(S);
    tempIdx = (tempIdx + K) % 7;
    return date[tempIdx];
    // Implement your solution here
}

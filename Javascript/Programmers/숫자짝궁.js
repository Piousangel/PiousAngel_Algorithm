function solution(X, Y) {
    let answer = '';
    
    let temp = [];
    // let XArr = Array.from(X);
    // let YArr = Array.from(Y);
    
    for(let i = 0; i < X.length; i++){    
        if (Y.includes(X[i])){
            temp.push(X[i]);
            Y = Y.substring(0, j) + Y.substring(j+1);
            break;
        }       
    }
   
    if (temp.length === 0) return "-1";
    answer = temp.sort((a,b) => b - a).join("");
    answer = Number(answer) === 0 ? "0" : answer
    return answer;
}
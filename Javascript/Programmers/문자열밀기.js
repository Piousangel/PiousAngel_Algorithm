function solution(A, B) {
    var answer = 0;
    let sumtempStr = A;
    for (let i = 0; i < A.length; i++) {
        if (sumtempStr === B) {
            return answer
        }
        let tempStr = sumtempStr.slice(0, A.length-1)
        sumtempStr = sumtempStr[A.length-1] + tempStr
        answer += 1
        
    }
    if (answer = A.length -1)
        answer = -1
    
    return answer;
}
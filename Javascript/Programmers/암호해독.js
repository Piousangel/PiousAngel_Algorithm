function solution(cipher, code) {
    
    let arr = [...cipher];
    let answer = arr.filter((t, idx) => (idx+1) % code === 0).join(''); 
    return answer;
}
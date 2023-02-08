function solution(s, skip, index) {
    let answer = '';
    let alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    
    let arr = alpha.filter((ch) => {
        return !skip.includes(ch);
    })
    
    for(let i = 0; i < s.length; i++){
        const tempIdx = (arr.indexOf(s[i]) + index) % arr.length;
        answer += arr[tempIdx];
    }
    
    return answer;
}
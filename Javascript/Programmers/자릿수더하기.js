function solution(n) {
    var answer = 0;
    const n_list = n.toString().split('');
    for(const num of n_list){
        answer += parseInt(num);
    }
    return answer;
}
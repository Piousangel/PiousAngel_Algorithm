function solution(my_string) {
    var answer = '';
    const strMyString = my_string.split('')
    const reverseStr = strMyString.reverse()
    answer = reverseStr.join('')
    return answer;
}
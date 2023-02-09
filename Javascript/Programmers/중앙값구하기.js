function solution(array) {
    let answer = 0;
    array.sort((a, b) => {
        return a - b;
    });
    // const value = array.length % 2 === 0 ? parseInt(array.length/2) + 1 : parseInt(array.length/2) ;
    return array[parseInt(array.length / 2)];
}

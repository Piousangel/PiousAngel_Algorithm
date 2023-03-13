// A, B가 서로 선호할 때 무료 식사 쿠폰을 제공
// 서로 선호하는 관계가 몇개인지 리턴
function solution(p) {
    let answer = 0;

    const map = new Map();
    const visited = [];

    for(const arr of p){
        map.set(arr[0], []);
    }
    
    for(const arr of p){
        const tempArr = map.get(arr[0]);
        tempArr.push(arr[1]);
        map.set(arr[0], tempArr);  
    }

    for (const items of map){
        for(const num of items[1]){
            if(!visited.includes(num)){
                if(map.get(num).includes(items[0])){
                    answer += 1;
                }
            }
        }
        visited.push(items[0]);
    }
    return answer;
}// A, B가 서로 선호할 때 무료 식사 쿠폰을 제공
// 서로 선호하는 관계가 몇개인지 리턴
function solution(p) {
    let answer = 0;

    const map = new Map();
    const visited = [];

    for(const arr of p){
        map.set(arr[0], []);
    }
    
    for(const arr of p){
        const tempArr = map.get(arr[0]);
        tempArr.push(arr[1]);
        map.set(arr[0], tempArr);  
    }

    for (const items of map){
        for(const num of items[1]){
            if(!visited.includes(num)){
                if(map.get(num).includes(items[0])){
                    answer += 1;
                }
            }
        }
        visited.push(items[0]);
    }
    return answer;
}
// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
// Q3
function solution(S) {
    const tempArr = S.split("\n")
    let picMap = new Map();
    let answer = '';
     
    for(let i = 0; i < tempArr.length; i++){
        let section = tempArr[i].split(", ");
        let location = section[1];
        if (picMap.has(location)) {
            let temp = picMap.get(location);
            picMap.set(location, [...picMap.get(location) , section[2]]);
        }
        else {
            picMap.set(location, [section[2]])
        }
    }

    for (let item of picMap){
        picMap.set(item[0],item[1].sort((a, b) => new Date(a) - new Date(b)) );
    }
    // console.log("123123", picMap)

     for(let i = 0; i < tempArr.length; i++){
        let section = tempArr[i].split(", ");
        let expansion = section[0].split('.')[1];
        let location = section[1];
        let date = section[2];
        // console.log(expansion)
        let name = '';
        const dateArr = picMap.get(location).indexOf(section[2]);
        if (picMap.get(location).length + 1 >= 10){
            if(dateArr + 1 < 10){
                name = location + '0' + String(dateArr+1) + '.' + expansion;
            }
            else{
                name = location + String(dateArr+1) + '.' + expansion;
            }          
        }
        else{
            name = location + String(dateArr+1) + '.' + expansion;
        }
        if(i !== tempArr.length - 1){
            answer += name+"\n";
        }
        else
            answer += name;
        
    }
    // console.log(answer)
    return answer;
}
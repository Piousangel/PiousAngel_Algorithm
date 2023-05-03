// re
function solution(players, callings) {
    const answer = [];
    const playerMap = new Map();
    
    for(let i = 0; i < players.length; i++){
        playerMap.set(players[i], i);
    }
    
    for(let i = 0; i < callings.length; i++){
        const targetIndex = playerMap.get(callings[i]);
        
        for (const [key, value] of playerMap) {
            if(value === targetIndex - 1){
                playerMap.set(key, playerMap.get(key) + 1);
                playerMap.set(callings[i], playerMap.get(callings[i]) - 1);
                continue;
            }
            
        }
    }
    
    let sortedArr = new Map([...playerMap].sort((a, b) => a[1] - b[1] ));
    for (const [key, value] of sortedArr) {
        answer.push(key);
    }
    
    return answer;
}
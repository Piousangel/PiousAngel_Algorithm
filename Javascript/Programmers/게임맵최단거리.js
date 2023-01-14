function solution(maps) {
    let answer = 1;
    let visited = maps;
    let queue = [];
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const row = maps.length;
    const col = maps[0].length;
    
    queue.push([0, 0]);
    visited[0][0] = 0;
    
    while(queue.length > 0) {
        let size = queue.length;
        
        for(let i = 0; i < size; i++) {
            let [y, x] = queue.shift();
            
            for(let j = 0; j < 4; j++) {
                let nx = x + dx[j];
                let ny = y + dy[j];
                
                if(nx >= 0 && nx < col && ny >= 0 && ny < row && visited[ny][nx] === 1) {
                    if(nx == col - 1 && ny == row - 1) {
                        return ++answer;
                    }
                    queue.push([ny, nx]);
                    visited[ny][nx] = 0;
                }
            }
        }
        answer++;
    }
    
    return -1;
}
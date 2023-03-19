function solution(arr) {

    const answer = [0, 0];
    const m = arr.length;
    
    const dfs = (nx, ny, length) => {
        const temp = arr[nx][ny];
        const half = Math.floor(length / 2);
        
        for(let i = nx; i < nx + length; i++){
            for(let j = ny; j < ny + length; j++){
                if(arr[i][j] !== temp){
                    dfs(nx, ny, half);
                    dfs(nx + half, ny, half);
                    dfs(nx, ny + half, half);
                    dfs(nx + half, ny + half, half);
                    return;
                }
            }
        }
        
        answer[temp]++;
    }
    
    dfs(0, 0, m);
    return answer;
}
// 같은 색 구슬 2개로 다른 구슬 1개로 바꿀 수 있음
// 빨간색 구슬 2개 -> 파란색 또는 초록색 1개
// 다른 색도 마찬가지
// 빨강 : a개, 파랑 : b개, 초록 : c 개 에서 d,e,f 개로 가지고 싶은데
// 가능한지 안한지 
// 이것도 완탐 돌리면 될 것 같은뎀

function dfs(arr) {

    if(arr[0] + arr[1] + arr[2] < arr[3] + arr[4] + arr[5]){
        return
    }
    if(arr[0] + arr[1] + arr[2] >= arr[3] + arr[4] + arr[5]){
        if(arr[0] >= arr[3] && arr[1] >= arr[4] && arr[2] >= arr[5]){
            answer = true;
            return
        }
    }

    for(let i = 0; i < 3; i++){
        if(arr[i] >= 2){
            if(i === 0){
                dfs([...arr].splice(0,3,arr[0]-2, arr[1]+1, arr[2]));
                dfs([...arr].splice(0,3,arr[0]-2, arr[1], arr[2]+1));
            }
            else if(i === 1){
                dfs([...arr].splice(0,3,arr[0]+1, arr[1]-2, arr[2]));
                dfs([...arr].splice(0,3,arr[0], arr[1]-2, arr[2]+1));
            }
            else{
                dfs([...arr].splice(0,3,arr[0]+1, arr[1], arr[2]-2));
                dfs([...arr].splice(0,3,arr[0], arr[1]+1, arr[2]-2));
            }
        }
    }
}
let answer = false;

function solution(a, b, c, d, e, f){
   
    let arr = [a,b,c,d,e,f];

    dfs(arr);

    return answer;
}
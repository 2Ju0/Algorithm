function solution(progresses, speeds) {
    var answer = [];
    let days = [];
    
    for(let i = 0; i < progresses.length; i++){
        let cnt = 1;
        while(true){
            if(progresses[i] + speeds[i] * cnt >= 100){
                days.push(cnt);
                break;
            }
            cnt += 1;
        }
    }
    
    let prev = days[0];
    let sumOfFunc = 1;
    
    for(let i = 1; i < days.length; i++){
        let cur = days[i];
        if(prev < cur){
            answer.push(sumOfFunc);
            sumOfFunc = 1;
            prev = cur;
        }
        else sumOfFunc += 1;
    }
    answer.push(sumOfFunc);
    
    return answer;
}
function solution(progresses, speeds) {
    var answer = [];
    let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]));
    
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
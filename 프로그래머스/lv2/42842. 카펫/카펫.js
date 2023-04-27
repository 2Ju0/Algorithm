function getDevisor(num) {
    let answer = []
    
    for(let i = 1; i < Number.parseInt(Math.sqrt(num)) + 1; i++){
        if(num % i === 0) answer.push([i, Number.parseInt(num / i)]);
    }
    return answer
}

function solution(brown, yellow) {
    var answer = [];
    const devisors = getDevisor(yellow);
    
    for(let devisor of devisors){
        let row = devisor[0];
        let column = devisor[1];
        let sum = (row + 2) * 2 + (column * 2);
        
        if (sum === brown) answer = [column + 2, row + 2];
    }
    return answer;
}
function getGCD(a, b) {
    let answer = 1;
    
    if(a % b === 0) answer = b;
    else if(b % a === 0) answer = a;
    else{
        for(let i = 2; i <= Math.min(a, b); i++){
            if(a % i === 0 && b % i === 0) answer = i;
        }
    }
    return answer;
}

function solution(arr) {
    while(arr.length !== 1){
        let a = arr.shift();
        let b = arr.shift();
        let gcd = getGCD(a, b);
        
        if(gcd === 1) arr.push(a * b);
        else arr.push(gcd * parseInt(a / gcd) * parseInt(b / gcd));
    }
    return arr.shift();
}
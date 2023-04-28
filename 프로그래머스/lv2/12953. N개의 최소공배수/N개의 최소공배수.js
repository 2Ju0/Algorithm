function getGCD(a, b) {
    let gcd = 1;
    
    if(a % b === 0) gcd = b;
    else if(b % a === 0) gcd = a;
    else{
        for(let i = 2; i <= Math.min(a, b); i++){
            if(a % i === 0 && b % i === 0) gcd = i;
        }
    }
    return gcd;
}

function solution(arr) {
    while(arr.length !== 1){
        let a = arr.shift();
        let b = arr.shift();
        let gcd = getGCD(a, b);
        
        if(gcd === 1) arr.push(a * b);
        else arr.push(a * b / gcd);
    }
    return arr.shift();
}
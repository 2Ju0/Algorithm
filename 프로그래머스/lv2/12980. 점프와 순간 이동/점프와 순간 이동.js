function solution(n) {
    if(n === 1) return 1;
    if(n % 2 === 0) return solution(n / 2);
    else return solution((n - 1) / 2) + 1;
}
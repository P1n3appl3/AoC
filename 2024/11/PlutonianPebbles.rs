fn main() {
    let input = std::fs::read_to_string("example").unwrap();
    let mut stones: Vec<i64> =
        input.split_whitespace().map(str::parse).map(Result::unwrap).collect();
    for _ in 0..25 {
        for i in 0..stones.len() {
            if stones[i] == 0 {
                stones[i] = 1;
            } else {
                let digits = stones[i].ilog10() + 1;
                if digits % 2 == 0 {
                    let new = stones[i] % 10i64.pow(digits / 2);
                    stones.push(new);
                    stones[i] /= 10i64.pow(digits / 2);
                } else {
                    stones[i] *= 2024;
                }
            }
        }
    }
    println!("{}", stones.len());
}

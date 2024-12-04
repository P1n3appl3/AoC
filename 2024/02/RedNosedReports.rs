fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let input: Vec<Vec<i8>> = input
        .lines()
        .map(|line| line.split_whitespace().map(|s| s.parse().unwrap()).collect())
        .collect();
    fn close(n: i8) -> bool {
        (1..=3).contains(&n.abs())
    }
    let ans = input
        .iter()
        .map(|report| {
            report
                .windows(2)
                .map(|window| {
                    let &[a, b] = window else { unreachable!() };
                    a - b
                })
                .collect()
        })
        .filter(|l: &Vec<i8>| {
            l.iter().copied().all(close)
                && l.iter()
                    .copied()
                    .map(i8::signum)
                    .collect::<Vec<_>>()
                    .windows(2)
                    .all(|w| w[0] == w[1])
        })
        .count();
    println!("{ans}");
}

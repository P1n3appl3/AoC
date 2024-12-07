fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let equations: Vec<(u64, Vec<u32>)> = input
        .lines()
        .map(|s| s.split_once(':').unwrap())
        .map(|(l, r)| {
            (
                l.parse().unwrap(),
                r.split_whitespace().map(str::parse).map(Result::unwrap).collect(),
            )
        })
        .collect();

    let solve = |p2| {
        equations
            .iter()
            .filter(|&(target, l)| {
                let [head, tail @ ..] = l.as_slice() else { panic!() };
                works(*target, *head as u64, tail, p2)
            })
            .map(|(target, _)| target)
            .sum::<u64>()
    };
    println!("{}", solve(false));
    println!("{}", solve(true));
}

fn works(target: u64, cur: u64, rest: &[u32], p2: bool) -> bool {
    if let [head, tail @ ..] = rest {
        works(target, cur * *head as u64, tail, p2)
            || works(target, cur + *head as u64, tail, p2)
            || p2 && works(target, format!("{cur}{head}").parse().unwrap(), tail, p2)
    } else {
        target == cur
    }
}

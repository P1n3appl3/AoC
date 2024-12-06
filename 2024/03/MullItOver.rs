pub fn solve(mut cur: &str, dodont: bool) -> u32 {
    let mut sum = 0;
    loop {
        let Some(i) = cur.find("mul(") else { break };
        if dodont {
            if let Some(j) = cur.find("don't()") {
                if j < i {
                    let Some(i) = cur.find("do()") else { break };
                    cur = &cur[i + 4..];
                    continue;
                }
            }
        }
        cur = &cur[i + 4..];
        let Some(i) = cur.find(',') else { break };
        let Ok(lhs) = cur[..i].parse::<u32>() else { continue };
        let rest = &cur[i + 1..];
        let Some(i) = rest.find(')') else { break };
        let Ok(rhs) = rest[..i].parse::<u32>() else { continue };
        sum += rhs * lhs;
        cur = &rest[i + 1..];
    }
    sum
}

fn main() {
    let input = std::fs::read_to_string("input").unwrap();

    let ans = solve(&input, false);
    println!("{ans}");
    let ans = solve(&input, true);
    println!("{ans}");
}

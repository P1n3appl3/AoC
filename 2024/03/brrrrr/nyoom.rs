mod mine;

use regex::{Captures, Regex};

use std::sync::LazyLock;

static RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"mul\((\d+),(\d+)\)").unwrap());
const IN: &str = include_str!("input");

fn solve_regex(input: &str) -> u32 {
    fn mul(c: Captures) -> u32 {
        let (_, [lhs, rhs]) = c.extract();
        lhs.parse::<u32>().unwrap() * rhs.parse::<u32>().unwrap()
    }
    RE.captures_iter(input).map(mul).sum()
}
fn solve_p2_regex(input: &str) -> u32 {
    let mut splits = input.split("don't()");
    let mut sum = solve_regex(splits.next().unwrap());
    for s in splits {
        if let Some(i) = s.find("do()") {
            sum += solve_regex(&s[i + 4..])
        }
    }
    sum
}

fn main() {
    assert_eq!(solve_regex(IN), mine::solve(IN, false));

    assert_eq!(solve_p2_regex(IN), mine::solve(IN, true));

    divan::main();
}

mod part_1 {
    use super::*;

    #[divan::bench]
    fn regex() -> u32 {
        solve_regex(IN)
    }

    #[divan::bench]
    fn mine() -> u32 {
        mine::solve(IN, false)
    }
}

mod part_2 {
    use super::*;

    #[divan::bench]
    fn regex() -> u32 {
        solve_p2_regex(IN)
    }

    #[divan::bench]
    fn mine() -> u32 {
        mine::solve(IN, true)
    }
}

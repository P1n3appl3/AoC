use std::{
    collections::HashMap,
    ops::{Add, BitOr},
};

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let (towels, patterns) = input.split_once("\n\n").unwrap();
    let mut towels: Vec<_> = towels.split(", ").collect();
    towels.sort_unstable_by_key(|n| n.len());
    let patterns = patterns.lines();
    let ans: u64 =
        patterns.clone().map(|p| solve(p, &towels, &mut HashMap::new(), u64::bitor)).sum();
    println!("{ans}");
    let ans: u64 = patterns.map(|p| solve(p, &towels, &mut HashMap::new(), u64::add)).sum();
    println!("{ans}");
}

fn solve<'a>(
    cur: &'a str,
    towels: &[&str],
    memo: &mut HashMap<&'a str, u64>,
    f: fn(u64, u64) -> u64,
) -> u64 {
    if cur.is_empty() {
        1
    } else if let Some(&n) = memo.get(cur) {
        n
    } else {
        towels
            .iter()
            .filter_map(|t| cur.strip_prefix(t))
            .map(|s| solve(s, towels, memo, f))
            .reduce(f)
            .inspect(|&n| _ = memo.insert(cur, n))
            .unwrap_or_default()
    }
}

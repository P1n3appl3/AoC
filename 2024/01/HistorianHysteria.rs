use std::{collections::HashMap, fs};

fn main() {
    let input = fs::read_to_string("input").unwrap();
    let (mut a, mut b): (Vec<_>, Vec<_>) = input
        .lines()
        .map(|l| {
            let [a, b] =
                l.split_whitespace().map(|i| i.parse::<i32>().unwrap()).collect::<Vec<_>>()
                    [..]
            else {
                panic!("oops")
            };
            (a, b)
        })
        .unzip();
    a.sort();
    b.sort();
    let sum = a.iter().zip(&b).map(|(&a, &b)| (a - b).abs()).sum::<i32>();
    let mut counts = HashMap::new();
    println!("{sum}");
    let sum = a
        .into_iter()
        .map(|n| {
            n as usize
                * *counts.entry(n).or_insert_with(|| b.iter().filter(|&&m| n == m).count())
        })
        .sum::<usize>();
    // dbg!(&counts);
    println!("{sum}");
}

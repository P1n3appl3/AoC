use std::array;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    // let groups: Vec<[String; 5]> = input
    //     .split("\n\n")
    //     .map(|s| array::from_fn(|i| s[i..].chars().step_by(6).collect()))
    //     .collect();
    let (locks, keys): (Vec<_>, Vec<_>) =
        input.split("\n\n").partition(|s| s.starts_with("....."));
    let parse = |s: &str| {
        array::from_fn(|i| {
            s[i..].chars().step_by(6).map(|b| (b == '#') as u8).sum::<u8>() - 1
        })
    };
    let locks: Vec<[u8; 5]> = locks.into_iter().map(parse).collect();
    let keys: Vec<[u8; 5]> = keys.into_iter().map(parse).collect();
    let ans: usize = locks
        .iter()
        .map(|l| {
            keys.iter().filter(|k| l.iter().zip(k.iter()).all(|(l, k)| l + k < 6)).count()
        })
        .sum();
    println!("{ans}");
}

use std::collections::HashMap;
use std::fs::File;
use std::io::Read;

fn simulate(state: &Vec<char>, patterns: &HashMap<&str, char>, generations: i64) -> i128 {
    let mut seen = HashMap::new();
    let mut state = state.clone();
    let mut zero = 0;
    for i in 0..generations {
        // Pad both sides
        let size = std::cmp::min(4, state.len());
        while state[..size].iter().any(|&c| c == '#') {
            state.insert(0, '.');
            zero += 1;
        }
        while state[state.len() - size..].iter().any(|&c| c == '#') {
            state.push('.');
        }
        zero -= 2;
        state = state
            .windows(5)
            .map(|frame| {
                patterns
                    .get(&frame.iter().collect::<String>().as_str())
                    .unwrap()
                    .clone()
            })
            .collect();
        let temp = state.iter().collect::<String>();
        if seen.contains_key(temp.as_str()) {
            zero -= generations - i - 1;
            break;
        }
        seen.insert(temp, (i, zero));
    }
    // println!("{}", state.iter().collect::<String>());
    // println!("{}", zero);
    // println!("{:?}", patterns);
    state
        .iter()
        .enumerate()
        .filter(|(_, &c)| c == '#')
        .map(|(n, _)| n as i128 - zero as i128)
        .sum::<i128>()
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let mut input = input.lines();
    let state = input
        .next()
        .unwrap()
        .split_whitespace()
        .nth(2)
        .unwrap()
        .chars()
        .collect::<Vec<_>>();
    let patterns: HashMap<_, _> = input
        .skip(1)
        .map(|s| {
            let mut temp = s.split_whitespace();
            (
                temp.next().unwrap(),
                temp.nth(1).unwrap().chars().next().unwrap(),
            )
        })
        .collect();
    println!("20 generations: {}", simulate(&state, &patterns, 20));
    println!(
        "50000000000 generations: {}",
        simulate(&state, &patterns, 50000000000)
    );
}

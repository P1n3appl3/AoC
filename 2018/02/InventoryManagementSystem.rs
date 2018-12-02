use std::fs::File;
use std::io::Read;

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let mut twos = 0;
    let mut threes = 0;
    for line in input.lines() {
        let mut two = false;
        let mut three = false;
        for letter in b'a'..=b'z' {
            match line.matches(letter as char).count() {
                2 => two = true,
                3 => three = true,
                _ => {}
            }
        }
        if two {
            twos += 1;
        }
        if three {
            threes += 1;
        }
    }
    println!(
        "twos: {}, threes: {}, checksum: {}",
        twos,
        threes,
        twos * threes
    );

    let mut lines = input.lines().collect::<Vec<&str>>();
    let full_len = lines[0].len();
    lines.sort();
    for pair in lines.windows(2) {
        let d = pair[0]
            .chars()
            .zip(pair[1].chars())
            .filter(|(a, b)| a == b)
            .map(|(a, _)| a)
            .collect::<String>();
        if d.len() == full_len - 1 {
            println!("common: {}", d);
        }
    }
}

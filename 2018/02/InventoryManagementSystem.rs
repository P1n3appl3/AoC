use std::fs::File;
use std::io::Read;

fn diff(s1: &str, s2: &str) -> String {
    s1.chars()
        .zip(s2.chars())
        .filter(|x| x.0 == x.1)
        .map(|x| x.0)
        .collect::<String>()
}

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
        "Twos: {}, Threes: {}, Checksum: {}",
        twos,
        threes,
        twos * threes
    );

    let lines = input.lines().collect::<Vec<&str>>();
    let full_len = lines[0].len();
    for i in 0..lines.len() - 1 {
        for j in i + 1..lines.len() {
            let d = diff(lines[i], lines[j]);
            if d.len() == full_len - 1 {
                println!("a: {}, b:{}, diff: {}", lines[i], lines[j], d);
            }
        }
    }
}

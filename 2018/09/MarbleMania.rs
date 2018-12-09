#![feature(try_reserve)]
use std::fs::File;
use std::io::Read;

fn solve(players: u32, last_marble: u32) -> u32 {
    let mut scores = vec![0; players as usize];
    let mut marbles = vec![0u32];
    let mut pos = 0;
    for marble in 1..=last_marble {
        match marble % 23 {
            0 => {
                pos = (pos + marbles.len() * 7 - 7) % marbles.len();
                scores[((marble - 1) % players) as usize] += marble + marbles[pos];
                marbles.remove(pos);
            }
            _ => {
                pos = (pos + 1) % marbles.len() + 1;
                marbles.insert(pos, marble);
            }
        }
    }
    *scores.iter().max().unwrap()
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();
    let mut input = input.split_whitespace();

    let players = input.next().unwrap().parse().unwrap();
    let last = input.nth(5).unwrap().parse().unwrap();
    println!("max score: {}", solve(players, last));
    println!("x100: {}", solve(players, 100*last));
}

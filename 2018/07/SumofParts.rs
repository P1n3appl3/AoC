use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::Read;

fn next_available(taken: &HashSet<char>, reqs: &HashMap<char, HashSet<char>>) -> Option<char> {
    (b'A'..=b'Z')
        .map(|l| l as char)
        .find(|l| !taken.contains(&l) && (!reqs.contains_key(l) || reqs.get(l).unwrap().is_empty()))
}

fn retire(letter: char, reqs: &mut HashMap<char, HashSet<char>>) {
    for l in b'A'..=b'Z' {
        reqs.entry(l as char).or_default().remove(&letter);
    }
}

#[derive(Clone)]
struct Progress {
    time: u8,
    target: char,
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let mut all_reqs = HashMap::new();
    for (after, before) in input.lines().map(|s| {
        let mut temp = s.split_whitespace();
        (
            temp.nth(1).unwrap().chars().next().unwrap(),
            temp.nth(5).unwrap().chars().next().unwrap(),
        )
    }) {
        all_reqs
            .entry(before)
            .or_insert(HashSet::new())
            .insert(after);
    }
    let mut reqs = all_reqs.clone();
    let mut taken = HashSet::new();
    print!("order: ");
    for _ in 0..26 {
        let next = next_available(&taken, &reqs).unwrap();
        taken.insert(next);
        print!("{}", next);
        retire(next, &mut reqs);
    }
    println!("");

    let mut reqs = all_reqs.clone();
    taken.clear();
    let mut workers = vec![
        Progress {
            time: 0,
            target: '.',
        };
        5
    ];
    let mut time = 0;
    while taken.len() < 26 {
        for w in &mut workers {
            match w.time {
                0 => {}
                1 => {
                    retire(w.target, &mut reqs);
                    w.target = '.';
                    w.time = 0;
                }
                _ => w.time -= 1,
            }
        }
        for w in workers.iter_mut().filter(|w| w.time == 0) {
            if let Some(next) = next_available(&taken, &reqs) {
                w.target = next;
                w.time = 61 + next as u8 - 'A' as u8;
                taken.insert(next);
            }
        }
        // println!(
        //     "{:04} - {}",
        //     time,
        //     workers.iter().map(|x| x.target).collect::<String>()
        // );
        time += 1;
    }
    // println!("\n...\n");
    println!(
        "time: {}",
        time + workers.iter().map(|w| w.time).max().unwrap() as u16 - 1
    );
}

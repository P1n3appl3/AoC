use std::collections::HashSet;
use std::fs::File;
use std::io::Read;

fn main() {
    let mut contents = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut contents).unwrap();

    let numbers: Vec<i32> = contents
        .lines()
        .map(|n| n.parse::<i32>().unwrap())
        .collect();
    println!("{}", numbers.iter().sum::<i32>());

    let mut seen = HashSet::new();
    let mut current = 0;
    'bigloop: loop {
        for num in numbers.iter() {
            seen.insert(current);
            current += num;
            if seen.contains(&current) {
                println!("Saw {} for a second time", current);
                break 'bigloop;
            }
        }
    }
}

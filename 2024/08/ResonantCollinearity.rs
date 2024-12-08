use std::collections::{HashMap, HashSet};

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let mut antennas: HashMap<char, HashSet<_>> = HashMap::new();
    let h = input.lines().count() as i16;
    let w = input.find('\n').unwrap() as i16;
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c != '.' {
                antennas.entry(c).or_default().insert((x as i16, y as i16));
            }
        }
    }
    let mut part1 = HashSet::new();
    let mut part2 = HashSet::new();
    let inside = |(x, y)| (0..w).contains(&x) && (0..h).contains(&y);
    for (_k, v) in antennas {
        for &a in &v {
            for &b in &v {
                if a == b {
                    continue;
                }
                let diff = (a.0 - b.0, a.1 - b.1);
                let n1 = (a.0 + diff.0, a.1 + diff.1);
                if inside(n1) {
                    part1.insert(n1);
                }
                let n2 = (b.0 - diff.0, b.1 - diff.1);
                if inside(n2) {
                    part1.insert(n2);
                }
                let d = diff;
                let mut pos = a;
                while inside(pos) {
                    pos = (pos.0 - d.0, pos.1 - d.1)
                }
                while {
                    pos = (pos.0 + d.0, pos.1 + d.1);
                    inside(pos)
                } {
                    part2.insert(pos);
                }
            }
        }
    }
    println!("{}", part1.len());
    println!("{}", part2.len());
    // println!();
    // for y in 0..h {
    //     for x in 0..w {
    //         if part2.contains(&(x, y)) {
    //             print!("#");
    //         } else {
    //             print!(".");
    //         }
    //     }
    //     println!()
    // }
}

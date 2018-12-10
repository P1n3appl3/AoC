use std::collections::HashSet;
use std::fs::File;
use std::io::Read;
use std::iter::FromIterator;

#[derive(Clone, Debug)]
struct Point {
    x: i32,
    y: i32,
    vx: i32,
    vy: i32,
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let mut points = input
        .lines()
        .map(|l| Point {
            x: l[10..16].trim().parse().unwrap(),
            y: l[17..24].trim().parse().unwrap(),
            vx: l[36..38].trim().parse().unwrap(),
            vy: l[39..42].trim().parse().unwrap(),
        })
        .collect::<Vec<_>>();
    let mut flag = false;
    let mut counter = 0;
    let threshold = 80;
    loop {
        for p in &mut points {
            p.x += p.vx;
            p.y += p.vy
        }
        counter += 1;
        let x_max = points.iter().map(|p| p.x).max().unwrap();
        let x_min = points.iter().map(|p| p.x).min().unwrap();
        let y_max = points.iter().map(|p| p.y).max().unwrap();
        let y_min = points.iter().map(|p| p.y).min().unwrap();
        println!("counter: {}", counter);
        println!("dimensions: {}, {}", x_max - x_min, y_max - y_min);
        if x_max - x_min < threshold {
            flag = true;
            let frame: HashSet<(i32, i32)> =
                HashSet::from_iter(points.iter().cloned().map(|p| (p.x, p.y)));
            println!("\nSTARTING NEW FRAME\n");
            for y in y_min..=y_max {
                for x in x_min..=x_max {
                    print!("{}", if frame.contains(&(x, y)) { '█' } else { ' ' });
                }
                println!();
            }
        } else if flag {
            break;
        }
    }
}

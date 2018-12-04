use std::fs::File;
use std::io::Read;
use std::str::Split;

#[derive(Debug)]
struct Square {
    id: u16,
    x: usize,
    y: usize,
    w: usize,
    h: usize,
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let mut board = [[0u16; 1000]; 1000];
    let mut squares = Vec::new();
    for line in input.lines() {
        let parse_int = |x: &mut Split<char>| x.next().unwrap().parse::<usize>().unwrap();
        let mut s = line.split(' ');
        let id = s.next().unwrap().trim_matches('#').parse::<u16>().unwrap();
        let mut pos = s.nth(1).unwrap().trim_matches(':').split(',');
        let x = parse_int(&mut pos);
        let y = parse_int(&mut pos);
        let mut dist = s.next().unwrap().split('x');
        let w = parse_int(&mut dist);
        let h = parse_int(&mut dist);
        squares.push(Square {
            id: id,
            x: x,
            y: y,
            w: w,
            h: h,
        });
    }

    for s in &squares {
        for i in 0..s.w {
            for j in 0..s.h {
                board[s.x + i][s.y + j] += 1;
            }
        }
    }
    println!(
        "covered twice: {}",
        board
            .iter()
            .map(|row| row.iter().filter(|cell| **cell > 1).count())
            .sum::<usize>()
    );

    let intersect = |a: &Square, b: &Square| {
        !(a.x > b.x + b.w || a.y > b.y + b.h || b.x > a.x + a.w || b.y > a.y + a.h)
    };
    'outer: for i in 0..squares.len() {
        for j in 0..squares.len() {
            if intersect(&squares[i], &squares[j]) && i != j {
                continue 'outer;
            }
        }
        println!("unique id: {}", squares[i].id);
    }
}

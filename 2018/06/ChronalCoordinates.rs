use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::Read;

fn check_point(pos: (i32, i32), coords: &HashMap<(i32, i32), u16>) -> u16 {
    let mut temp = coords
        .iter()
        .map(|(coord, n)| ((pos.0 - coord.0).abs() + (pos.1 - coord.1).abs(), *n))
        .collect::<Vec<_>>();
    temp.sort();
    if temp[0].0 == temp[1].0 {
        return 0;
    }
    return temp[0].1;
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let coords = input.lines().map(|x| {
        let mut temp = x.split(',');
        (
            temp.next().unwrap().trim().parse::<i32>().unwrap(),
            temp.next().unwrap().trim().parse::<i32>().unwrap(),
        )
    });
    let ymin = coords.clone().map(|(_, y)| y).min().unwrap();
    let xmin = coords.clone().min().unwrap().0;
    let ymax = coords.clone().map(|(_, y)| y).max().unwrap();
    let xmax = coords.clone().max().unwrap().0;
    let mut current = 0;
    let coords = coords
        .map(|(x, y)| {
            current += 1;
            ((x - xmin, y - ymin), current)
        })
        .collect::<HashMap<(i32, i32), u16>>();

    let mut border = HashSet::new();
    let mut board = Vec::with_capacity(xmax as usize);
    for x in 0..xmax {
        board.push(vec![0; ymax as usize]);
        for y in 0..ymax {
            board[x as usize][y as usize] = check_point((x, y), &coords);
            if x <= 0 || x >= xmax - 1 || y <= 0 || y >= ymax - 1 {
                border.insert(board[x as usize][y as usize]);
            }
        }
    }

    // let visual: Vec<char> = " ,./<>?!@#$%^&*(~)`QWERTYU,IOPA-SDFGHJKLZXCVBNM_+{}"
    //     .chars()
    //     .collect();
    // for x in 0..xmax as usize {
    //     board.push(vec![0; ymax as usize]);
    //     for y in 0..ymax as usize {
    //         print!("{}", visual[board[x][y] as usize]);
    //     }
    //     println!("");
    // }

    println!(
        "largest area: {}",
        (1..=current)
            .filter(|x| !border.contains(x))
            .map(|n| board
                .iter()
                .map(|row| row.iter().filter(|x| **x == n).count())
                .sum::<usize>())
            .max()
            .unwrap()
    );
    let mut sum = 0;
    for x in 0..xmax {
        for y in 0..ymax {
            if coords
                .iter()
                .map(|((x2, y2), _)| (x - x2).abs() + (y - y2).abs())
                .sum::<i32>()
                < 10000
            {
            sum += 1
            }
        }
    }
    println!("safe area: {}", sum);
}

use std::{
    cmp::Reverse,
    collections::{BinaryHeap, HashMap, HashSet},
};

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let board: Vec<Vec<_>> = input.lines().map(|line| line.bytes().collect()).collect();
    let (height, width) = (board.len() as i32, board[0].len() as i32);
    let (start, end) = ((1, height - 2), (width - 2, 1));
    let mut seen = HashMap::new();
    let mut todo = BinaryHeap::from([Reverse((0, start, (1, 0), vec![]))]);
    let mut max = i32::MAX;
    let mut best = HashSet::from([start]);
    while let Some(Reverse((score, cur @ (x, y), prev, path))) = todo.pop() {
        if score > max {
            break;
        }
        if cur == end {
            max = score;
            best.extend(path);
            continue;
        }
        seen.insert((cur, prev), score);
        for dir @ (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
            let new @ (x, y) = (x + dx, y + dy);
            if board[y as usize][x as usize] == b'#' {
                continue;
            }
            let new_score = score + 1 + 1000 * (dir != prev) as i32;
            if let Some(&n) = seen.get(&(new, dir)) {
                if new_score > n {
                    continue;
                }
            }
            let mut path = path.clone();
            path.push(new);
            todo.push(Reverse((new_score, new, dir, path)));
        }
    }
    println!("{max}");
    println!("{}", best.len());
}

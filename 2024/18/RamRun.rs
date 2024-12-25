use std::collections::{HashSet, VecDeque};

const SIZE: usize = 70;
const TAKE: usize = 1024;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let coords: Vec<i8> = input
        .lines()
        .flat_map(|l| l.split(','))
        .map(str::parse)
        .map(Result::unwrap)
        .collect();
    let coords: Vec<_> = coords.chunks_exact(2).map(|c| (c[0], c[1])).collect();
    println!("{}", bfs(&coords[..TAKE]).unwrap());

    let mut range = TAKE..coords.len();
    while range.len() > 1 {
        let mid = (range.start + range.end) / 2;
        range =
            if bfs(&coords[..mid]).is_some() { mid..range.end } else { range.start..mid };
    }
    let (x, y) = coords[range.start];
    println!("{x},{y}");
}

fn bfs(coords: &[(i8, i8)]) -> Option<usize> {
    let corrupted: HashSet<_> = coords.iter().copied().collect();
    let mut seen = HashSet::new();
    let mut todo = VecDeque::from([((0, 0), 0)]);
    while let Some((pos @ (x, y), dist)) = todo.pop_front() {
        if !((0..=SIZE as i8).contains(&x) && (0..=SIZE as i8).contains(&y))
            || seen.contains(&pos)
            || corrupted.contains(&pos)
        {
            continue;
        }
        seen.insert(pos);
        if pos == (SIZE as i8, SIZE as i8) {
            return Some(dist);
        }
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
            todo.push_back(((x + dx, y + dy), dist + 1));
        }
    }
    None
}

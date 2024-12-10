use std::collections::{HashSet, VecDeque};

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let map: Vec<Vec<u8>> = input.lines().map(|s| s.as_bytes().to_vec()).collect();

    let (w, h) = (map[0].len() as i8, map.len() as i8);
    let mut p1 = 0;
    let mut p2 = 0;
    for y in 0..h {
        for x in 0..w {
            if map[y as usize][x as usize] == b'0' {
                p1 += search((x, y), (w, h), &map, true);
                p2 += search((x, y), (w, h), &map, false);
            }
        }
    }

    println!("{p1} {p2}");
}

fn inside((x, y): (i8, i8), (w, h): (i8, i8)) -> bool {
    (0..w).contains(&x) && (0..h).contains(&y)
}

fn search(pos: (i8, i8), size: (i8, i8), map: &[Vec<u8>], p1: bool) -> u16 {
    let mut reached = 0;
    let mut seen = HashSet::from([pos]);
    let mut q = VecDeque::from([(pos, b'0')]);
    while let Some(((x, y), cur)) = q.pop_front() {
        if cur == b'9' {
            reached += 1;
            continue;
        }
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
            let next = (x + dx, y + dy);
            if inside(next, size)
                && !(p1 && seen.contains(&next))
                && map[next.1 as usize][next.0 as usize] == cur + 1
            {
                q.push_back((next, cur + 1));
                seen.insert(next);
            }
        }
    }
    reached
}

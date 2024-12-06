use std::collections::HashSet;

fn main() {
    let input = std::fs::read_to_string("example").unwrap();
    let mut walls = HashSet::new();
    let mut visited = HashSet::new();
    let mut pos = (0, 0);
    let offset = [(0, -1), (1, 0), (0, 1), (-1, 0)];
    let mut dir = 0;
    let h = input.lines().count() as i32;
    let w = input.find('\n').unwrap() as i32;
    for (y, line) in input.lines().enumerate() {
        for (x, b) in line.bytes().enumerate() {
            match b {
                b'#' => {
                    walls.insert((x as i32, y as i32));
                }
                b'^' => {
                    pos = (x as i32, y as i32);
                }
                _ => {}
            }
        }
    }

    while (0..w).contains(&pos.0) && (0..h).contains(&pos.1) {
        visited.insert((pos, dir));
        let (x, y) = pos;
        let (dx, dy) = offset[dir];
        let new = (x + dx, y + dy);
        if walls.contains(&new) {
            dir = (dir + 1) % 4;
            continue;
        }
        pos = new;
    }
    println!("{}", visited.len());

    let ans = visited
        .iter()
        .filter(|((x, y), dir)| {
            let right = (dir + 1) % 4;
            let (dx, dy) = offset[right];
            let new = (x + dx, y + dy);
            if visited.contains(&(new, right)) {
                println!("{new:?}");
                true
            } else {
                false
            }
        })
        .count();
    println!("{ans}");
}

use std::collections::HashSet;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let mut walls = HashSet::new();
    let mut visited = HashSet::new();
    let offset = [(0, -1), (1, 0), (0, 1), (-1, 0)];
    let mut pos = (0i16, 0i16);
    let mut dir = 0u8;
    let h = input.lines().count() as i16;
    let w = input.find('\n').unwrap() as i16;
    for (y, line) in input.lines().enumerate() {
        for (x, b) in line.bytes().enumerate() {
            match b {
                b'#' => {
                    walls.insert((x as i16, y as i16));
                }
                b'^' => {
                    pos = (x as i16, y as i16);
                }
                _ => {}
            }
        }
    }

    let start = pos;
    let inside = |(x, y)| (0..w).contains(&x) && (0..h).contains(&y);
    let next = |((x, y), dir)| {
        let (dx, dy) = offset[dir as usize];
        (x + dx, y + dy)
    };
    let step = |(pos, dir), walls: &HashSet<_>| {
        let new = next((pos, dir));
        if walls.contains(&new) { (pos, (dir + 1) % 4) } else { (new, dir) }
    };

    let mut part2 = 0;
    while inside(pos) {
        let front = next((pos, dir));
        'part2: {
            if inside(front) && !walls.contains(&front) {
                for i in 0..4 {
                    if visited.contains(&(front, i)) {
                        break 'part2;
                    }
                }
                let mut visited = visited.clone();
                let (mut pos, mut dir) = (pos, dir);

                walls.insert(front);
                while inside(pos) {
                    visited.insert((pos, dir));
                    (pos, dir) = step((pos, dir), &walls);
                    if visited.contains(&(pos, dir)) {
                        part2 += 1;
                        // show(front, start, (w, h), &walls, &visited);
                        break;
                    }
                }
                walls.remove(&front);
            }
        }

        visited.insert((pos, dir));
        (pos, dir) = step((pos, dir), &walls);
    }

    println!("{}", visited.iter().map(|(pos, _dir)| pos).collect::<HashSet<_>>().len());
    println!("{part2}");
}

fn show(
    new_wall: (i16, i16),
    start: (i16, i16),
    (w, h): (i16, i16),
    walls: &HashSet<(i16, i16)>,
    s: &HashSet<((i16, i16), u8)>,
) {
    println!();
    for y in 0..h {
        for x in 0..w {
            let pos = (x, y);
            if pos == new_wall {
                print!("O");
            } else if walls.contains(&pos) {
                print!("#")
            } else if pos == start {
                print!("^")
            } else {
                let h = s.contains(&(pos, 1)) || s.contains(&(pos, 3));
                let v = s.contains(&(pos, 0)) || s.contains(&(pos, 2));
                match (h, v) {
                    (true, true) => print!("+"),
                    (true, false) => print!("-"),
                    (false, true) => print!("|"),
                    (false, false) => print!("."),
                }
            }
        }
        println!();
    }
    println!();
}

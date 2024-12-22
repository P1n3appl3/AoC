use std::collections::{HashMap, VecDeque};

fn main() {
    let mut buf = String::new();
    let input = std::fs::read_to_string("input").unwrap();
    let (map, dirs) = input.split_once("\n\n").unwrap();
    let mut board = HashMap::new();
    let mut pos = (0, 0);
    let dimensions @ (w, h) =
        (map.lines().count() as i32, map.lines().next().unwrap().len() as i32);
    for (y, line) in map.lines().enumerate() {
        for (x, c) in line.bytes().enumerate() {
            let p = (x as i32, y as i32);
            match c {
                b @ (b'#' | b'O') => {
                    board.insert(p, b);
                }
                b'@' => pos = p,
                b'.' => (),
                _ => panic!(),
            };
        }
    }
    let original = board.clone();
    let start = pos;
    for dir in dirs.bytes() {
        let new = r#move(pos, dir);

        // draw(pos, dimensions, &board);
        // std::io::stdin().read_line(&mut buf).ok();
        // println!("\n{}", dir as char);
        // println!("new: {new:?} ({:?})", board.get(&new).map(|&b| b as char));
        match board.get(&new) {
            Some(b'O') => {
                let mut end = new;
                loop {
                    end = r#move(end, dir);
                    match board.get(&end) {
                        Some(b'#') => break,
                        None => {
                            board.remove(&new);
                            board.insert(end, b'O');
                            pos = new;
                            break;
                        }
                        Some(_) => (),
                    }
                }
            }
            None => pos = new,
            Some(_) => (),
        }
    }

    // draw(pos, dimensions, &board);
    let ans: i32 =
        board.iter().filter_map(|((x, y), &b)| (b == b'O').then_some(y * 100 + x)).sum();
    println!("{ans}");

    let mut board: HashMap<(i32, i32), u8> = original
        .iter()
        .flat_map(|(&(x, y), &b)| {
            let &[l, r] = if b == b'O' { b"[]" } else { b"##" };
            [((x * 2, y), l), ((x * 2 + 1, y), r)].into_iter()
        })
        .collect();
    let dimensions = (w * 2, h);
    pos = (start.0 * 2, start.1);

    for dir in dirs.bytes() {
        let new = r#move(pos, dir);
        //
        // draw(pos, dimensions, &board);
        // std::io::stdin().read_line(&mut buf).ok();
        // println!("\n{}", dir as char);
        // println!("new: {new:?} ({:?})", board.get(&new).map(|&b| b as char));

        match board.get(&new) {
            Some(b'[' | b']') => {
                if if dir <= b'>' {
                    push_h(new, dir, &mut board)
                } else {
                    push_v(new, dir, &mut board)
                } {
                    pos = new
                }
            }
            None => pos = new,
            Some(_) => (),
        }
    }
    // draw(pos, dimensions, &board);
    let ans: i32 =
        board.iter().filter_map(|((x, y), &b)| (b == b'[').then_some(y * 100 + x)).sum();
    println!("{ans}");
}

fn r#move((x, y): (i32, i32), dir: u8) -> (i32, i32) {
    match dir {
        b'<' => (x - 1, y),
        b'>' => (x + 1, y),
        b'^' => (x, y - 1),
        b'v' => (x, y + 1),
        _ => (x, y),
    }
}

fn push_h(pos: (i32, i32), dir: u8, board: &mut HashMap<(i32, i32), u8>) -> bool {
    let mut new = pos;
    loop {
        new = r#move(new, dir);
        match board.get(&new) {
            Some(b'#') => return false,
            None => {
                let rev = dir ^ 0b10;
                while new != pos {
                    let prev = r#move(new, rev);
                    board.insert(new, board[&prev]);
                    new = prev;
                }
                board.remove(&pos);
                return true;
            }
            Some(_) => (),
        }
    }
}

fn push_v(pos: (i32, i32), dir: u8, board: &mut HashMap<(i32, i32), u8>) -> bool {
    let mut todo = VecDeque::from([pos]);
    let mut seen = vec![];
    while let Some(cur) = todo.pop_front() {
        if seen.contains(&cur) {
            continue;
        }
        match board.get(&cur) {
            Some(c) if b"[]".contains(c) => {
                seen.push(cur);
                let new = (cur.0 + if *c == b'[' { 1 } else { -1 }, cur.1);
                todo.push_back(new);
                todo.push_back(r#move(cur, dir));
            }
            Some(b'#') => return false,
            None => (),
            Some(_) => unreachable!(),
        };
    }
    // println!("{:?}", &seen);
    for pos in seen.into_iter().rev() {
        let prev = board[&pos];
        board.insert(r#move(pos, dir), prev);
        board.remove(&pos);
    }
    true
}

fn draw(pos: (i32, i32), (w, h): (i32, i32), board: &HashMap<(i32, i32), u8>) {
    for y in 0..h {
        for x in 0..w {
            print!("{}", match board.get(&(x, y)) {
                Some(&b) => b as char,
                None =>
                    if pos.0 == x && pos.1 == y {
                        '@'
                    } else {
                        '.'
                    },
            })
        }
        println!()
    }
}

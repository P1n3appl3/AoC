use std::collections::HashMap;
use std::convert::From;
use std::fs::File;
use std::io::Read;

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn next_dir(d: Direction) -> Direction {
    match d {
        Direction::Left => Direction::Up,
        Direction::Up => Direction::Right,
        Direction::Right => Direction::Left,
        _ => panic!("can't turn 180"),
    }
}

fn turn(current: Direction, turn_dir: Direction) -> Direction {
    use Direction::*;
    match (current, turn_dir) {
        (Up, x) => x,
        (x, Up) => x,
        (Down, Left) => Right,
        (Left, Left) => Down,
        (Right, Left) => Up,
        (Down, Right) => Left,
        (Left, Right) => Up,
        (Right, Right) => Down,
        (_, Down) => panic!("can't turn 180 ({:?} -> {:?})", current, turn_dir),
    }
}

impl From<char> for Direction {
    fn from(item: char) -> Self {
        match item {
            '^' => Direction::Up,
            'v' => Direction::Down,
            '<' => Direction::Left,
            '>' => Direction::Right,
            _ => panic!("invalid direction: {}", item),
        }
    }
}

#[derive(Debug, Eq, PartialEq, Ord, PartialOrd)]
struct Cart {
    y: usize,
    x: usize,
    dir: Direction,
    last_turn: Direction,
    dead: bool,
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let mut board = HashMap::new();
    let mut carts = Vec::new();
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            match c {
                '^' | 'v' | '<' | '>' => {
                    carts.push(Cart {
                        y: y,
                        x: x,
                        dir: c.into(),
                        last_turn: Direction::Right,
                        dead: false,
                    });
                }
                '\\' | '/' | '+' => {
                    board.insert((x, y), c);
                }
                _ => {}
            };
        }
    }

    while carts.len() > carts.iter().filter(|x| x.dead).count() + 1 {
        use Direction::*;
        carts.sort();
        // draw(&board, &carts);
        for i in 0..carts.len() {
            if carts[i].dead {
                continue;
            }
            match board.get(&(carts[i].x, carts[i].y)) {
                Some('\\') => {
                    carts[i].dir = turn(
                        carts[i].dir,
                        match carts[i].dir {
                            Up | Down => Left,
                            Left | Right => Right,
                        },
                    )
                }
                Some('/') => {
                    carts[i].dir = turn(
                        carts[i].dir,
                        match carts[i].dir {
                            Up | Down => Right,
                            Left | Right => Left,
                        },
                    )
                }
                Some('+') => {
                    carts[i].last_turn = next_dir(carts[i].last_turn);
                    carts[i].dir = turn(carts[i].dir, carts[i].last_turn);
                }
                _ => {}
            };
            match carts[i].dir {
                Up => carts[i].y -= 1,
                Down => carts[i].y += 1,
                Left => carts[i].x -= 1,
                Right => carts[i].x += 1,
            };
            for j in 0..carts.len() {
                if !carts[j].dead && j != i && carts[i].x == carts[j].x && carts[i].y == carts[j].y
                {
                    carts[i].dead = true;
                    carts[j].dead = true;
                    println!("Collision at: {},{}", carts[i].x, carts[i].y);
                }
            }
        }
    }
    let alive = carts
        .iter()
        .enumerate()
        .filter(|(_, c)| !c.dead)
        .map(|(pos, _)| pos)
        .next()
        .unwrap();
    println!("Last one at: {},{}", carts[alive].x, carts[alive].y);
}

fn draw(board: &HashMap<(usize, usize), char>, carts: &Vec<Cart>) {
    let (width, height) = (48, 85);
    let (x, y) = (10, 20);
    println!(
        "{}",
        (y..y + width)
            .map(|y| (x..x + height)
                .map(move |x| {
                    if let Some(temp) = carts.iter().find_map(|c| {
                        if c.x == x && c.y == y && !c.dead {
                            Some(match c.dir {
                                Direction::Up => '^',
                                Direction::Down => 'v',
                                Direction::Left => '<',
                                Direction::Right => '>',
                            })
                        } else {
                            None
                        }
                    }) {
                        temp
                    } else if let Some(&temp) = board.get(&(x, y)) {
                        if temp != '+' {
                            temp
                        } else {
                            ' '
                        }
                    } else {
                        ' '
                    }
                })
                .collect::<String>()
                + "\n")
            .collect::<String>()
    );
}

use std::collections::HashSet;

const W: i32 = 101;
const H: i32 = 103;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    fn parse(line: &str) -> [i32; 4] {
        let numbers: Vec<i32> =
            line.split(&['=', ',', ' ']).filter_map(|s| s.parse().ok()).collect();
        numbers.as_slice().try_into().expect("{numbers:?}")
    }
    let bots: Vec<_> = input.lines().map(parse).collect();
    let ans: i32 = quadrants(&frame(100, &bots)).iter().product();
    println!("{ans}");

    // thx to Dan for cluing me in to the upper bound
    'outer: for i in 0..(W * H) {
        let bots = frame(i, &bots);
        let positions: HashSet<_> = bots.iter().map(|&[x, y, _, _]| (x, y)).collect();
        for x in 0..W {
            for y in 0..H {
                if (0..10).all(|n| positions.contains(&(x, y + n))) {
                    // draw(&bots);
                    println!("{i}");
                    break 'outer;
                }
            }
        }
    }
}

fn frame(i: i32, bots: &[[i32; 4]]) -> Vec<[i32; 4]> {
    bots.iter()
        .map(|&[x, y, dx, dy]| {
            [(x + dx * i).rem_euclid(W), (y + dy * i).rem_euclid(H), dx, dy]
        })
        .collect()
}

fn quadrants(bots: &[[i32; 4]]) -> [i32; 4] {
    let mut quadrants = [0; 4];
    for &[x, y, _, _] in bots {
        if x == W / 2 || y == H / 2 {
            continue;
        };
        let q = (y > H / 2) as usize * 2 + (x > W / 2) as usize;
        quadrants[q] += 1
    }
    quadrants
}

fn draw(bots: &[[i32; 4]]) {
    println!("P1");
    println!("{W} {H}");
    let positions: HashSet<_> = bots.iter().map(|&[x, y, _, _]| (x, y)).collect();
    for y in 0..H {
        for x in 0..W {
            if positions.contains(&(x, y)) { print!("0") } else { print!("1") }
        }
        println!();
    }
}
// do any formats support 1bpp "monow" pix_fmt?
// | ffmpeg -i - -r 10 -c:v libx264 -qp 0 -pix_fmt gray output.mp4
// mpv --scale=nearest !$

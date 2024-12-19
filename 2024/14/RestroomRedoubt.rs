use std::collections::HashSet;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let (w, h) = (101, 103);
    let mut quadrants = [0; 4];
    let mut bots: Vec<[_; 4]> = Vec::new();
    for line in input.lines() {
        let numbers: Vec<i32> =
            line.split(&['=', ',', ' ']).filter_map(|s| s.parse().ok()).collect();
        let bot @ &[x, y, dx, dy] = numbers.as_slice() else { unreachable!("{numbers:?}") };
        bots.push(bot.try_into().unwrap());
        let (x, y) = ((x + dx * 100).rem_euclid(w), (y + dy * 100).rem_euclid(h));
        if x == w / 2 || y == h / 2 {
            continue;
        };
        let q = (y > h / 2) as usize * 2 + (x > w / 2) as usize;
        quadrants[q] += 1
    }
    // let ans: i32 = quadrants.iter().product();
    // println!("{ans}");

    // thx to Dan for cluing me in to the upper bound
    for _ in 0..(w * h) {
        println!("P1");
        println!("{w} {h}");
        let positions: HashSet<_> = bots.iter().map(|arr| (arr[0], arr[1])).collect();
        for y in 0..h {
            for x in 0..w {
                if positions.contains(&(x, y)) { print!("0") } else { print!("1") }
            }
            println!();
        }
        // println!("{i}");
        bots.iter_mut().for_each(|arr| {
            arr[0] = (arr[0] + arr[2]).rem_euclid(w);
            arr[1] = (arr[1] + arr[3]).rem_euclid(h);
        });
    }
}
// do any formats support 1bpp "monow" pix_fmt?
// | ffmpeg -i - -c:v libx264 -qp 0 -pix_fmt gray output.mp4
// mpv --scale=nearest !$

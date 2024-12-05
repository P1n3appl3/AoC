fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let input: Vec<Vec<u8>> = input.lines().map(|line| line.bytes().collect()).collect();
    let mut ans1 = 0;
    let mut ans2 = 0;
    let height = input.len();
    let width = input[0].len();
    for y in 0..height {
        for x in 0..width {
            if x < width - 3 {
                if &input[y][x..x + 4] == b"XMAS" {
                    ans1 += 1;
                }
                if &input[y][x..x + 4] == b"SAMX" {
                    ans1 += 1;
                }
            }

            if y >= 3
                && x < width - 3
                && (input[y][x] == b'X'
                    && input[y - 1][x + 1] == b'M'
                    && input[y - 2][x + 2] == b'A'
                    && input[y - 3][x + 3] == b'S'
                    || input[y][x] == b'S'
                        && input[y - 1][x + 1] == b'A'
                        && input[y - 2][x + 2] == b'M'
                        && input[y - 3][x + 3] == b'X')
            {
                ans1 += 1;
            }

            if y < height - 3 {
                if input[y][x] == b'X'
                    && input[y + 1][x] == b'M'
                    && input[y + 2][x] == b'A'
                    && input[y + 3][x] == b'S'
                    || input[y][x] == b'S'
                        && input[y + 1][x] == b'A'
                        && input[y + 2][x] == b'M'
                        && input[y + 3][x] == b'X'
                {
                    ans1 += 1;
                }

                if x < width - 3
                    && (input[y][x] == b'X'
                        && input[y + 1][x + 1] == b'M'
                        && input[y + 2][x + 2] == b'A'
                        && input[y + 3][x + 3] == b'S'
                        || input[y][x] == b'S'
                            && input[y + 1][x + 1] == b'A'
                            && input[y + 2][x + 2] == b'M'
                            && input[y + 3][x + 3] == b'X')
                {
                    ans1 += 1;
                }
            }
            if x <= width - 3
                && y <= height - 3
                && input[y + 1][x + 1] == b'A'
                && (input[y][x] == b'M' && input[y + 2][x + 2] == b'S'
                    || input[y][x] == b'S' && input[y + 2][x + 2] == b'M')
                && (input[y + 2][x] == b'M' && input[y][x + 2] == b'S'
                    || input[y + 2][x] == b'S' && input[y][x + 2] == b'M')
            {
                ans2 += 1;
            }
        }
    }
    println!("{ans1}");
    println!("{ans2}");
}

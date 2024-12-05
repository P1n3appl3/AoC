fn main() {
    let input = std::fs::read_to_string("example").unwrap();
    let input: Vec<Vec<u8>> = input.lines().map(|line| line.bytes().collect()).collect();
    let mut ans = 0;
    let height = input.len();
    let width = input[0].len();
    let mut board = vec![vec![b'.'; width]; height];
    for y in 0..height {
        // println!("{y}");
        for x in 0..width {
            // println!("  {x}");
            if x < width - 3 {
                if &input[y][x..x + 4] == b"XMAS" {
                    // println!("FOUND: {x} {y}");
                    ans += 1;
                    board[y][x..x + 4].copy_from_slice(b"XMAS");
                }
                if &input[y][x..x + 4] == b"SAMX" {
                    // println!("FOUND: {x} {y}");
                    ans += 1;
                    board[y][x..x + 4].copy_from_slice(b"SAMX");
                }
            }

            if y >= 3 && x < width - 3 {
                if input[y][x] == b'X'
                    && input[y - 1][x + 1] == b'M'
                    && input[y - 2][x + 2] == b'A'
                    && input[y - 3][x + 3] == b'S'
                {
                    // println!("FOUND: {x} {y}");
                    ans += 1;
                    board[y][x] = b'X';
                    board[y - 1][x + 1] = b'M';
                    board[y - 2][x + 2] = b'A';
                    board[y - 3][x + 3] = b'S';
                }

                if input[y][x] == b'S'
                    && input[y - 1][x + 1] == b'A'
                    && input[y - 2][x + 2] == b'M'
                    && input[y - 3][x + 3] == b'X'
                {
                    // println!("FOUND: {x} {y}");
                    board[y][x] = b'S';
                    board[y - 1][x + 1] = b'A';
                    board[y - 2][x + 2] = b'M';
                    board[y - 3][x + 3] = b'X';
                    ans += 1;
                }
            }

            if y < height - 3 {
                if input[y][x] == b'X'
                    && input[y + 1][x] == b'M'
                    && input[y + 2][x] == b'A'
                    && input[y + 3][x] == b'S'
                {
                    // println!("FOUND: {x} {y}");
                    board[y][x] = b'X';
                    board[y + 1][x] = b'M';
                    board[y + 2][x] = b'A';
                    board[y + 3][x] = b'S';
                    ans += 1;
                }

                if input[y][x] == b'S'
                    && input[y + 1][x] == b'A'
                    && input[y + 2][x] == b'M'
                    && input[y + 3][x] == b'X'
                {
                    // println!("FOUND: {x} {y}");
                    ans += 1;
                    board[y][x] = b'S';
                    board[y + 1][x] = b'A';
                    board[y + 2][x] = b'M';
                    board[y + 3][x] = b'X';
                }

                if x < width - 3 {
                    if input[y][x] == b'X'
                        && input[y + 1][x + 1] == b'M'
                        && input[y + 2][x + 2] == b'A'
                        && input[y + 3][x + 3] == b'S'
                    {
                        board[y][x] = b'X';
                        board[y + 1][x + 1] = b'M';
                        board[y + 2][x + 2] = b'A';
                        board[y + 3][x + 3] = b'S';
                        // println!("FOUND: {x} {y}");
                        ans += 1;
                    }

                    if input[y][x] == b'S'
                        && input[y + 1][x + 1] == b'A'
                        && input[y + 2][x + 2] == b'M'
                        && input[y + 3][x + 3] == b'X'
                    {
                        board[y][x] = b'S';
                        board[y + 1][x + 1] = b'A';
                        board[y + 2][x + 2] = b'M';
                        board[y + 3][x + 3] = b'X';
                        // println!("FOUND: {x} {y}");
                        ans += 1;
                    }
                }
            }
        }
    }
    println!("{ans}");
    // println!();
    // for row in board {
    //     for c in row {
    //         print!("{}", c as char);
    //     }
    //     println!();
    // }
    // println!();
}

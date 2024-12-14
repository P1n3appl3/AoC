fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let numbers: Vec<i64> =
        input.split(&['+', '=', ',', '\n']).filter_map(|s| s.parse().ok()).collect();

    let ans: i64 = numbers.chunks(6).filter_map(solve::<false>).sum();
    println!("{ans}");
    let ans: i64 = numbers.chunks(6).filter_map(solve::<true>).sum();
    println!("{ans}");
}

#[rustfmt::skip]
fn solve<const P2: bool>(c: &[i64]) -> Option<i64> {
    let &[ax, ay, bx, by, mut x, mut y] = c else { unreachable!() };
    let big = 10_000_000_000_000; if P2 { x += big; y += big; }
    let det = ax * by - bx * ay;
    let (a, b) = (x * by - y * bx, y * ax - x * ay);
    (a % det == 0 && b % det == 0).then_some((3 * a + b) / det)
}

// https://www.3blue1brown.com/lessons/change-of-basis#going-from-ours-to-hers
//  ┌   ┐┌       ┐-1  ┌   ┐   ┌   ┐┌         ┐
//  │ x ││ ax bx │  _ │ a │ _ │ x ││  by -bx │ det ⁻¹
//  │ y ││ ay by │  ‾ │ b │ ‾ │ y ││ -ay  ax │
//  └   ┘└       ┘    └   ┘   └   ┘└         ┘

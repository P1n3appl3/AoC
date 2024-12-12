use std::collections::{BTreeSet, HashMap};

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let garden: HashMap<(i16, i16), u8> = input
        .lines()
        .enumerate()
        .flat_map(|(y, line)| {
            line.bytes().enumerate().map(move |(x, plant)| ((x as i16, y as i16), plant))
        })
        .collect();
    let mut todo: BTreeSet<_> = garden.keys().copied().collect();
    let mut total = 0;
    while let Some(pos) = todo.first().copied() {
        let (area, perimeter) = fill(pos, garden[&pos], &mut todo, &garden);
        total += area * perimeter;
    }
    println!("{total}");
}

#[rustfmt::skip]
fn fill(
    pos @ (x, y): (i16, i16), plant: u8,
    todo: &mut BTreeSet<(i16, i16)>, garden: &HashMap<(i16, i16), u8>,
) -> (u32, u32) {
    let Some(&p) = garden.get(&pos) else { return (0, 1) };
    if p != plant { return (0, 1); };
    if !todo.remove(&pos) { return (0, 0); };
    [(-1, 0), (0, -1), (1, 0), (0, 1)].iter()
        .map(|(dx, dy)| fill((x + dx, y + dy), p, todo, garden))
        .fold((1, 0), |(x, y), (dx, dy)| (x + dx, y + dy))
}

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
    let (mut p1, mut p2) = (0, 0);
    while let Some(pos) = todo.first().copied() {
        let mut edges = BTreeSet::new();
        let mut plant = BTreeSet::new();
        let (area, perimeter) =
            fill(pos, garden[&pos], &mut todo, &mut plant, &mut edges, &garden);
        p1 += area * perimeter;
        p2 += area * sides(&edges, &plant);
        // println!("{}: area: {} perimeter: {} sides: {}",
        //     garden[&pos] as char, area, perimeter, sides(&edges, &plant))
    }
    println!("{p1}");
    println!("{p2}");
}

#[rustfmt::skip]
fn fill(
    pos @ (x, y): (i16, i16), plant: u8,
            todo: &mut BTreeSet<(i16, i16)>,
             cur: &mut BTreeSet<(i16, i16)>,
           edges: &mut BTreeSet<(i16, i16)>,
          garden:      &HashMap<(i16, i16), u8>,
) -> (u32, u32) {
    let Some(&p) = garden.get(&pos) else { edges.insert(pos); return (0, 1); };
                    /*||*/ if p != plant { edges.insert(pos); return (0, 1); };
    if !todo.remove(&pos) { return (0, 0); };
    cur.insert(pos);
    [(-1, 0), (0, -1), (1, 0), (0, 1)]
        .iter()
        .map(|(dx, dy)| fill((x + dx, y + dy), p, todo, cur, edges, garden))
        .fold((1, 0), |(x, y), (dx, dy)| (x + dx, y + dy))
}

#[rustfmt::skip]
fn sides(edges: &BTreeSet<(i16, i16)>, plant: &BTreeSet<(i16, i16)>) -> u32 {
    edges.iter().copied().flat_map(|(x, y)| { [
        plant.contains(&(x + 1, y    )) && !(plant.contains(&(x + 1, y + 1)) && edges.contains(&(x,     y + 1))),
        plant.contains(&(x,     y + 1)) && !(plant.contains(&(x + 1, y + 1)) && edges.contains(&(x + 1, y    ))),
        plant.contains(&(x - 1, y    )) && !(plant.contains(&(x - 1, y - 1)) && edges.contains(&(x,     y - 1))),
        plant.contains(&(x,     y - 1)) && !(plant.contains(&(x - 1, y - 1)) && edges.contains(&(x - 1, y    ))),
    ].into_iter() })
    .filter(|&b| b)
    .count() as u32
}

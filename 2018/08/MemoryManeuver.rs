use std::fs::File;
use std::io::Read;

fn part1(list: &mut Iterator<Item = u32>) -> u32 {
    let children = list.next().unwrap();
    let metadata = list.next().unwrap() as usize;
    (0..children).map(|_| part1(list)).sum::<u32>() + list.take(metadata).sum::<u32>()
}

fn part2(list: &mut Iterator<Item = u32>) -> u32 {
    let children = list.next().unwrap();
    let metadata = list.next().unwrap();
    match children {
        0 => list.take(metadata as usize).sum(),
        _ => {
            let nodes = (0..children).map(|_| part2(list)).collect::<Vec<_>>();
            (0..metadata)
                .map(|_| list.next().unwrap() - 1)
                .filter(|&x| x < children)
                .map(|x| nodes[x as usize])
                .sum()
        }
    }
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let tree = input.split_whitespace().map(|x| x.parse().unwrap());

    println!("all metadata: {}", part1(&mut tree.clone().into_iter()));
    println!("sum of children: {}", part2(&mut tree.into_iter()));
}

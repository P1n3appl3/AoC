use std::{fs, iter};

fn main() {
    let input = fs::read_to_string("example").unwrap();
    let mut disk: Vec<u16> = input
        .replace('\n', "0")
        .as_bytes()
        .chunks_exact(2)
        .enumerate()
        .flat_map(|(id, pair)| {
            let [len, padding] = pair else { unreachable!() };
            iter::repeat(id as u16)
                .take((len - b'0') as usize)
                .chain(iter::repeat(u16::MAX).take((padding - b'0') as usize))
        })
        .collect();
    // println!("{disk:?}");
    let mut last_free = 0;
    while let Some(new) = disk[last_free..].iter().position(|&n| n == u16::MAX) {
        last_free += new;
        disk[last_free] = disk.pop().unwrap();
    }
    // println!("{disk:?}");
    let ans: usize = disk.iter().enumerate().map(|(i, &n)| i * n as usize).sum();
    println!("{ans}");
}

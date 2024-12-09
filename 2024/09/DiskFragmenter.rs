use std::{collections::BTreeSet, fs, iter};

fn main() {
    let input = fs::read_to_string("input").unwrap();
    let mut map: BTreeSet<_> = input
        .replace('\n', "0")
        .as_bytes()
        .chunks_exact(2)
        .enumerate()
        .scan(0, |cur, (id, pair)| {
            let [size, padding] = pair else { unreachable!() };
            let (size, padding) = ((size - b'0') as u32, (padding - b'0') as u32);
            let r = (*cur, size, id as u32);
            *cur += size + padding;
            Some(r)
        })
        .collect();
    let mut disk: Vec<u32> = map
        .iter()
        .scan(0, |cur, &(pos, size, id)| {
            let gap = pos - *cur;
            *cur = pos + size;
            let i = iter::repeat(u32::MAX)
                .take(gap as usize)
                .chain(iter::repeat(id).take(size as usize));
            Some(i)
        })
        .flatten()
        .collect();

    let mut last_free = 0;
    while let Some(new) = disk[last_free..].iter().position(|&n| n == u32::MAX) {
        last_free += new;
        disk[last_free] = disk.pop().unwrap();
    }
    let ans: usize = disk.into_iter().enumerate().map(|(i, n)| i * n as usize).sum();
    println!("{ans}");

    let mut done = BTreeSet::new();
    while let Some(seg @ (_pos, size, id)) = map.last().cloned() {
        if let Some(new) = next_free(size, &map) {
            map.insert((new, size, id));
        } else {
            done.insert(seg);
        }
        map.pop_last();
    }
    let ans: usize = done
        .into_iter()
        .flat_map(|(pos, len, id)| (pos..pos + len).map(move |n| (n * id) as usize))
        .sum();
    println!("{ans}");
}

fn next_free(width: u32, map: &BTreeSet<(u32, u32, u32)>) -> Option<u32> {
    map.iter()
        .scan(0, |cur, (s, size, _id)| {
            let old = *cur;
            let gap = s - old;
            *cur = s + size;
            Some((gap, old))
        })
        .find_map(|(size, pos)| (size >= width).then_some(pos))
}

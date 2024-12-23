use std::{
    collections::{HashMap, HashSet},
    fs,
};

fn valid(update: &[u32], rules: &HashMap<u32, HashSet<u32>>) -> bool {
    let mut seen = HashSet::new();
    for &n in update {
        if let Some(r) = rules.get(&n) {
            if !r.is_disjoint(&seen) {
                return false;
            }
        }
        seen.insert(n);
    }
    true
}

fn order(update: &[u32], transitive: &HashMap<u32, HashSet<u32>>) -> Vec<u32> {
    use std::cmp::Ordering;
    let mut new = update.to_vec();
    new.sort_by(|a, b| {
        if let Some(r) = transitive.get(a) {
            if r.contains(b) {
                return Ordering::Less;
            }
        }
        Ordering::Greater
    });
    new
}

fn main() {
    let input = fs::read_to_string("input").unwrap();
    let Some((relations, updates)) = input.split_once("\n\n") else { return };
    let mut rules: HashMap<u32, HashSet<u32>> = HashMap::new();
    relations
        .lines()
        .map(|rule| {
            rule.split('|')
                .map(str::parse)
                .map(Result::unwrap)
                .collect::<Vec<_>>()
                .try_into()
                .unwrap()
        })
        .for_each(|r: [u32; 2]| {
            rules.entry(r[0]).or_default().insert(r[1]);
        });
    let updates: Vec<Vec<u32>> = updates
        .lines()
        .map(|update| update.split(',').map(str::parse).map(Result::unwrap).collect())
        .collect();

    let ans: u32 =
        updates.iter().filter(|u| valid(u, &rules)).map(|u| u[u.len() / 2]).sum();
    println!("{ans}");

    let mut transitive = HashMap::new();
    for (k, v) in &rules {
        let mut cur = v.clone();
        let mut seen = HashSet::new();
        while seen != cur {
            let mut new: HashSet<u32> = HashSet::new();
            for &n in cur.difference(&seen) {
                if let Some(r) = rules.get(&n) {
                    new.extend(r);
                }
            }
            seen.extend(&cur);
            cur.extend(new);
        }
        transitive.insert(k, cur);
    }

    let ans: u32 = updates
        .iter()
        .filter(|u| !valid(u, &rules))
        .map(|u| order(u, &rules)[u.len() / 2])
        .sum();
    println!("{ans}");
}

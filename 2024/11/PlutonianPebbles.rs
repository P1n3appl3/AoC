use std::collections::HashMap;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let stones: Vec<i64> =
        input.split_whitespace().map(str::parse).map(Result::unwrap).collect();
    let ans: i64 = stones.iter().map(|&n| solve::<25>(n, 0, &mut HashMap::new())).sum();
    println!("{ans}");
    let ans: i64 = stones.iter().map(|&n| solve::<75>(n, 0, &mut HashMap::new())).sum();
    println!("{ans}");
}

fn solve<const K: u8>(n: i64, i: u8, seen: &mut HashMap<i64, HashMap<u8, i64>>) -> i64 {
    if i == K {
        return 1;
    }
    let i = i + 1;
    if let Some(&n) = seen.entry(n).or_default().get(&i) {
        return n;
    }
    let res = if n == 0 {
        solve::<K>(1, i, seen)
    } else {
        let digits = n.ilog10() + 1;
        if digits % 2 == 0 {
            let half = 10i64.pow(digits / 2);
            solve::<K>(n % half, i, seen) + solve::<K>(n / half, i, seen)
        } else {
            solve::<K>(n * 2024, i, seen)
        }
    };
    seen.get_mut(&n).unwrap().insert(i, res);
    res
}

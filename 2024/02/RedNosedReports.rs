fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let input: Vec<Vec<i8>> = input
        .lines()
        .map(|line| line.split_whitespace().map(|s| s.parse().unwrap()).collect())
        .collect();

    fn close(n: i8) -> bool {
        (1..=3).contains(&n.abs())
    }
    fn mono(a: i8, b: i8, lt: bool) -> bool {
        lt && a < b || !lt && a > b
    }
    fn strict(cur: i8, l: &[i8], lt: bool) -> bool {
        let &[head, ref rest @ ..] = l else { return true };
        l.is_empty() || close(cur - head) && mono(cur, head, lt) && strict(head, rest, lt)
    }

    let ans = input.iter().filter(|l| strict(l[0], &l[1..], l[0] < l[1])).count();
    println!("{ans}");

    fn lenient(cur: i8, l: &[i8], lt: bool) -> bool {
        let &[head, ref rest @ ..] = l else { return true };
        close(cur - head) && mono(cur, head, lt) && lenient(head, rest, lt)
            || strict(cur, rest, lt)
    }

    let ans = input
        .iter()
        .filter(|l| {
            lenient(l[0], &l[1..], l[0] < l[1]) || strict(l[1], &l[2..], l[1] < l[2])
        })
        .count();
    println!("{ans}");
}

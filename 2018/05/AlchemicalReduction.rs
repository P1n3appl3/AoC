use std::fs::File;
use std::io::Read;

fn react(p: &mut Vec<char>) -> usize {
    let mut pos = 1 as usize;
    while pos < p.len() {
        if p[pos].to_lowercase().next() == p[pos - 1].to_lowercase().next()
            && p[pos].is_lowercase() == p[pos - 1].is_uppercase()
        {
            p.remove(pos);
            p.remove(pos - 1);
            pos -= if pos == 1 { 1 } else { 2 };
        }
        pos += 1;
    }
    p.len()
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let chain = input.trim().chars().collect::<Vec<char>>();
    println!("length: {}", react(&mut chain.clone()));

    let mut improved = Vec::new();
    for letter in b'a'..=b'z' {
        let mut temp = chain.clone();
        temp.retain(|c| c.to_lowercase().next().unwrap() != letter as char);
        improved.push(react(&mut temp));
    }
    println!("smallest: {}", improved.iter().min().unwrap());
}

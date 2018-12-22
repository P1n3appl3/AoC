fn run_round(scores: &mut Vec<u8>, e1: usize, e2: usize) -> (usize, usize) {
    let new = scores[e1] + scores[e2];
    if new >= 10 {
        scores.push(1);
        scores.push(new - 10);
    } else {
        scores.push(new);
    }
    (
        (e1 + scores[e1] as usize + 1) % scores.len(),
        (e2 + scores[e2] as usize + 1) % scores.len(),
    )
}

fn main() {
    let input = 360781;
    let input_digits: Vec<u8> = input
        .to_string()
        .chars()
        .map(|c| c.to_digit(10).unwrap() as u8)
        .collect();
    let mut scores = vec![3u8, 7, 1, 0];
    let mut elf1 = 0;
    let mut elf2 = 1;
    while scores.len() < input + 10 {
        let temp = run_round(&mut scores, elf1, elf2);
        elf1 = temp.0;
        elf2 = temp.1;
    }
    println!(
        "next 10: {}",
        scores[input..input + 10]
            .iter()
            .map(|x| x.to_string())
            .collect::<String>()
    );
    if let Some((pos, _)) = scores
        .windows(input_digits.len())
        .enumerate()
        .find(|(_, digits)| {
            digits
                .iter()
                .zip(input_digits.iter())
                .all(|(&a, &b)| a == b)
        })
    {
        println!("first occurance at: {}", pos);
        return;
    }
    let mut pos = scores.len() - input_digits.len();
    loop {
        let temp = run_round(&mut scores, elf1, elf2);
        elf1 = temp.0;
        elf2 = temp.1;
        while pos < scores.len() - input_digits.len() {
            if scores[pos..]
                .iter()
                .zip(input_digits.iter())
                .all(|(&a, &b)| a == b)
            {
                println!("first occurance at: {}", pos);
                return;
            }
            pos += 1;
        }
        if pos % 1000000 == 0 {
            println!("{}", pos);
        }
    }
}

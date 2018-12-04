use std::collections::HashMap;
use std::fmt;
use std::fs::File;
use std::io::Read;
use std::str::FromStr;

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Event {
    Wake,
    Sleep,
    Start(u16),
}

impl FromStr for Event {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(match s.chars().nth(19).unwrap() {
            'f' => Event::Sleep,
            'w' => Event::Wake,
            _ => Event::Start(
                s.split_whitespace()
                    .nth(3)
                    .unwrap()
                    .trim_matches('#')
                    .parse::<u16>()
                    .unwrap(),
            ),
        })
    }
}

#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Time {
    year: u16,
    month: u8,
    day: u8,
    hour: u8,
    min: u8,
}

impl Time {
    fn diff(&self, other: &Self) -> u8 {
        if other.hour != self.hour {
            other.min + 60 - self.min
        } else {
            other.min - self.min
        }
    }
}

impl fmt::Debug for Time {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "[{}-{:02}-{:02} {:02}:{:02}]",
            self.year, self.month, self.day, self.hour, self.min
        )
    }
}

impl FromStr for Time {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Time {
            year: s[1..5].parse().unwrap(),
            month: s[6..8].parse().unwrap(),
            day: s[9..11].parse().unwrap(),
            hour: s[12..14].parse().unwrap(),
            min: s[15..17].parse().unwrap(),
        })
    }
}

fn main() {
    let mut input = String::new();
    let mut f = File::open("input.txt").unwrap();
    f.read_to_string(&mut input).unwrap();

    let mut events = input
        .lines()
        .map(|s| (s.parse::<Time>().unwrap(), s.parse::<Event>().unwrap()))
        .collect::<Vec<(Time, Event)>>();
    events.sort();

    let mut guards = HashMap::new();
    let mut current = 0;
    for i in 0..events.len() {
        let (ref t, ref e) = events[i];
        // print!("{:?} - {:?}", t, e);
        match e {
            Event::Start(g) => current = *g,
            // Event::Wake => println!("\t\t\tdurration: {}", events[i - 1].0.diff(t)),
            Event::Wake => *guards.entry(current).or_insert(0) += events[i - 1].0.diff(t) as usize,
            Event::Sleep => {}
        }
    }
    let sleepiest = guards.iter().map(|(a, b)| (*b, *a)).max().unwrap().1;
    println!("guard {} had the most sleep", sleepiest);

    let mut times = [0; 60];
    for i in 0..events.len() {
        let (ref t, ref e) = events[i];
        match e {
            Event::Start(g) => current = *g,
            Event::Sleep => {}
            Event::Wake => if current == sleepiest {
                for i in events[i - 1].0.min..t.min {
                    times[i as usize] += 1;
                }
            },
        }
    }
    let best_time = times
        .iter()
        .enumerate()
        .map(|(a, b)| (b, a))
        .max()
        .unwrap()
        .1;
    println!("best time: {}", best_time);
    println!("answer: {}", best_time * sleepiest as usize);

    let mut guards = HashMap::new();
    for i in 0..events.len() {
        let (ref t, ref e) = events[i];
        match e {
            Event::Start(g) => current = *g,
            Event::Wake => {
                let times = guards.entry(current).or_insert([0; 60]);
                for i in events[i - 1].0.min..t.min {
                    times[i as usize] += 1;
                }
            }
            Event::Sleep => {}
        }
    }
    let stuff = guards
        .iter()
        .map(|(id, times)| {
            let best_time = times.iter().enumerate().map(|(a, b)| (b, a)).max().unwrap();
            (best_time.0, best_time.1, id)
        }).max()
        .unwrap();

    println!(
        "guard {} sleeps through minute {} {} times",
        stuff.2, stuff.1, stuff.0
    );
    println!("answer: {}", stuff.1 * *stuff.2 as usize);
}

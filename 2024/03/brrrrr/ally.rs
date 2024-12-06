pub fn part1(bytes: &str) -> u32 {
    let mut total = 0;
    for s in bytes.split("mul(") {
        let Some(comma_ix) = s.find(',') else { continue };
        if !(1..=3).contains(&comma_ix) {
            continue;
        }
        let Ok(first) = str::parse::<i32>(&s[..comma_ix]) else { continue };
        let Some(paren_ix) = s.find(')') else { continue };
        if !(1..=3).contains(&(paren_ix - comma_ix - 1)) {
            continue;
        }
        let Ok(second) = str::parse::<i32>(&s[comma_ix + 1..paren_ix]) else { continue };

        total += first * second;
    }

    total as u32
}

pub fn part2(bytes: &str) -> u32 {
    let mut total = 0;
    let mut mul_enabled = true;
    for mut s in bytes.split("mul(") {
        'l: {
            let Some(comma_ix) = s.find(',') else {
                break 'l;
            };
            if !(1..=3).contains(&comma_ix) {
                break 'l;
            }
            let Ok(first) = str::parse::<i32>(&s[..comma_ix]) else {
                break 'l;
            };
            let Some(paren_ix) = s.find(')') else {
                break 'l;
            };
            if !(1..=3).contains(&(paren_ix - comma_ix - 1)) {
                break 'l;
            }
            let Ok(second) = str::parse::<i32>(&s[comma_ix + 1..paren_ix]) else {
                break 'l;
            };

            if mul_enabled {
                total += first * second;
            }
            break 'l;
        }
        loop {
            let do_ix = s.find("do()");
            let dont_ix = s.find("don't()");
            match (do_ix, dont_ix) {
                (Some(do_ix), Some(dont_ix)) => {
                    if do_ix < dont_ix {
                        mul_enabled = true;
                        s = &s[do_ix + 4..];
                    } else {
                        mul_enabled = false;
                        s = &s[dont_ix + 6..];
                    }
                }
                (Some(do_ix), None) => {
                    mul_enabled = true;
                    s = &s[do_ix + 4..];
                }
                (None, Some(dont_ix)) => {
                    mul_enabled = false;
                    s = &s[dont_ix + 6..];
                }
                (None, None) => {
                    break;
                }
            }
        }
    }

    total as u32
}

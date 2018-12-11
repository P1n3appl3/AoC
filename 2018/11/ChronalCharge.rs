fn main() {
    let serial_number = 9424;
    let mut grid = [[0i32; 300]; 300];
    for y in 0..300 {
        for x in 0..300 {
            let rack_id = x + 11;
            let power: i32 = rack_id * (y + 1);
            grid[x as usize][y as usize] = (power + serial_number) * rack_id / 100 % 10 - 5;
        }
    }

    let mut max = (0, 0, 0);
    for y in 0..298 {
        for x in 0..298 {
            let mut sum = 0;
            for yy in 0..3 {
                for xx in 0..3 {
                    sum += grid[x + xx][y + yy];
                }
            }
            if sum > max.0 {
                max = (sum, x + 1, y + 1);
            }
        }
    }
    println!("max coords: {},{}", max.1, max.2);

    let mut max = (0, 0, 0, 0);
    for n in 1..=300 {
        for y in 0..300 - n {
            for x in 0..300 - n {
                let mut sum = 0;
                for yy in 0..n {
                    for xx in 0..n {
                        sum += grid[x + xx][y + yy];
                    }
                }
                if sum > max.0 {
                    max = (sum, x + 1, y + 1, n);
                }
            }
        }
    }
    println!("max of any size: {},{},{}", max.1, max.2, max.3);
}

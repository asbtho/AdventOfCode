
use std::fs;
use std::time::Instant;

fn main() {
    let start = Instant::now(); 

    the_task();

    let duration = start.elapsed();
    println!("Function executed in: {:?}", duration);
}

fn the_task() {
    let instructions = read_text_file();

    let mut dial = 50;

    let mut password= 0;

    for string in &instructions {
        let (direction, number) = string.split_at(1);

        let number: i32 = number.trim().parse().unwrap();

        let mut zeros = 0;
        let sum;
        
        if direction == "R" {
            sum = dial + number;
        } else if direction == "L" {
            sum = dial - number;
        } else {
            panic!("Unknown direction");
        }

        if sum > 0 {
            zeros += sum / 100;
        } else if sum == 0 {
            zeros += 1;
        } else {
            zeros += ( (100 - dial) % 100 + number.abs() ) / 100;
        }

        dial = mathematical_modulo(sum, 100);

        password += zeros;
    }
    println!("Final Result: {}",password);
}

fn mathematical_modulo(a: i32, m: i32) -> i32 {
    let r = a % m;
    if r < 0 {
        r + m
    } else {
        r
    }
}

fn read_text_file() -> Vec<String> {
    let contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    let string_vector: Vec<String> = contents.split("\n").map(|s| s.to_string()).collect();

    return string_vector;
}

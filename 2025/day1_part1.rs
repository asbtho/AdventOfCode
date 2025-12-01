
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
        println!("{dial}");

        let (direction, number) = string.split_at(1);

        let number: i32 = number.trim().parse().unwrap();

        if direction == "R" {
            let sum = dial + number;
            dial = mathematical_modulo(sum, 100);
        } else if direction == "L" {
            let sum = dial - number;
            dial = mathematical_modulo(sum, 100);
        }

        if dial == 0 {
            password += 1;
        }
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
    let contents = fs::read_to_string("testinput.txt")
        .expect("Should have been able to read the file");

    let string_vector: Vec<String> = contents.split("\n").map(|s| s.to_string()).collect();

    return string_vector;
}

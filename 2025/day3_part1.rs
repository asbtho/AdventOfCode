
use std::fs;
use std::time::Instant;

fn main() {
    let start = Instant::now(); 

    the_task();

    let duration = start.elapsed();
    println!("Function executed in: {:?}", duration);
}

fn the_task() {
    let banks = read_text_file();

    let mut final_sum = 0;

    for bank in banks {
        let bank_vec: Vec<char> = bank.chars().collect();

        let mut number = 0;

        for i in 0..bank_vec.len() {
            for j in 0..bank_vec.len() {
                if i < j {
                    let s1 = bank_vec[i];
                    let s2 = bank_vec[j];
                    let s3 = format!("{}{}", s1, s2);
                    if number < s3.parse::<u64>().unwrap() {
                        number = s3.parse::<u64>().unwrap();
                    }
                }
            }
        }

        final_sum += number;
    }

    println!("Final sum: {}", final_sum);
}

fn read_text_file() -> Vec<String> {
    let contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    contents.split("\n").map(|s| s.trim().to_string() ).collect()
}

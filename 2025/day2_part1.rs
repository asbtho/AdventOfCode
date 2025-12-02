
use std::fs;
use std::time::Instant;

fn main() {
    let start = Instant::now(); 

    the_task();

    let duration = start.elapsed();
    println!("Function executed in: {:?}", duration);
}

fn the_task() {
    let ranges = read_text_file();

    let mut final_sum = 0;

    for range in ranges {
        let (first_id, last_id) = range.trim().split_once("-").unwrap();

        let first_id_num = first_id.parse::<u64>().unwrap();
        let last_id_num = last_id.parse::<u64>().unwrap();

        for i in first_id_num..last_id_num +1 {
            let s = i.to_string();
            let (s_first, s_last) = s.split_at(s.len() / 2);
            if s_first == s_last {
                final_sum += i;
            }
        }
    }

    println!("Final sum: {}", final_sum);
}

fn read_text_file() -> Vec<String> {
    let contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    let string_vector: Vec<String> = contents.split(",").map(|s| s.to_string()).collect();

    return string_vector;
}

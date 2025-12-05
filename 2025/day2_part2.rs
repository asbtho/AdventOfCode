
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

    let mut integer_vec = Vec::new();

    for (start, end) in ranges {
        for i in start..end + 1 {

            let mut number = i;

            while number != 0 {
                integer_vec.push((number % 10) as u8);
                number /= 10; 
            };

            let length = integer_vec.len();

            'outer:for j in 1..(length / 2) + 1 {

                let mut int = integer_vec.chunks(j);

                let first_chunk = int.next().unwrap();

                if int.all(|x| x == first_chunk) {
                    final_sum += i;
                    integer_vec.clear();
                    break 'outer;
                }
            }
            integer_vec.clear();
        }
    }

    println!("Final sum: {}", final_sum);
}

fn read_text_file() -> Vec<(u64, u64)> {
    let contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");

    contents.split(",").map(|s| { let (s1, s2) = s.trim().split_once("-").unwrap(); ( s1.parse().unwrap(), s2.parse().unwrap() ) }).collect()
}

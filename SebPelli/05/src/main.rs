use std::time::Instant;


//The idea of treating this as a binary string came from @Tommimon
//I had to go through lots of Reddit to learn most of these Rust functions
//And understand how to write a linear search in Rust for this problem. 


fn main()
{
    
    let start = Instant::now(); //I use this to count how long the program takes. If not interested, just remove it
    
    let mut boarding_passes = include_str!("/Users/sebastianpelli/Desktop/Advent/day5input.txt").lines()
                                                .map(|s| s.bytes()
                                                .fold(0, |a, x| 2 * a + (x == b'B' || x == b'R') as u32))
                                                .collect::<Vec<_>>();

    boarding_passes.sort_unstable();
    println!("{}", boarding_passes.last().unwrap());
    println!("{}", (boarding_passes[0] ..).zip(boarding_passes.into_iter())
    .find(|(s, t)| s != t)
    .unwrap().0);

    let duration = start.elapsed(); //I use this to count how long the program takes. If not interested, just remove it
    println!("Duration: {} us", duration.as_micros()); //I use this to count how long the program takes. If not interested, just remove it
}
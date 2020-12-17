use std::time::Instant;
use std::fs;
use std::collections::HashSet;
use std::iter::FromIterator;

fn part1 (input: &String) -> usize{
    
    let mut parsed = input.split("\n\n");

    let mut counter = 0;

    for group in parsed{
        let mut answers_given : Vec<_> = group.chars().filter(|c| c != &'\n').collect();
        answers_given.sort();
        answers_given.dedup();
        

        counter += answers_given.len();
    }

    return counter;
}

fn part2 (input: &String) ->usize{
    input.split("\n\n").map(|group| {
            group.lines()
                .map(|l| l.chars().collect::<HashSet<char>>())
                .fold(None, |maybe_set1: Option<HashSet<char>>, set2| {
                    maybe_set1
                        .map(|set1| set1.intersection(&set2).map(|c| *c).collect())
                        .or(Some(set2))
                })
                .unwrap()
                .len()
        })
        .sum()
}

fn main() {

    let start = Instant::now();
    let input = fs::read_to_string("/Users/sebastianpelli/Desktop/Advent/day6input.txt").unwrap();

    println!("Part 1: {}\n", part1(&input));
    println!("Part 2: {}\n", part2(&input));

    let duration = start.elapsed(); 
    println!("Duration: {} us", duration.as_micros());
}
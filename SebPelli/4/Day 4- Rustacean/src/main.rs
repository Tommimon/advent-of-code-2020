
use std::{fs::read_to_string, ops::RangeInclusive};


/*took the idea for Part1 from @mynam3isg00d*/
/*Had to go through lots of Reddit ideas to learn most of the Rust functions I used*/


fn main() {
    println!(
        "Number of valid passports (Part1): {}",
        std::fs::read_to_string("/Users/sebastianpelli/Desktop/Advent/vivalenin.txt")
            .unwrap()
            .split("\n\n")
            .filter(|passport| {
                let area = passport.split_whitespace();
                let fields = area.map(|field| field.split(":").next());
                fields.filter(|&key| key != Some("cid")).count() == 7
            })
            .count()
    );

    println!(
        "Number of valid passports (Part 2): {}",
        read_to_string("/Users/sebastianpelli/Desktop/Advent/vivalenin.txt")
            .unwrap()
            .split("\n\n")
            .filter(|passport| passport.split_whitespace().filter(is_valid_field).count() == 7)
            .count()
    );
}


/*self explanatory but anyway: checks the validity requirements for Part2*/

fn is_valid_field(field: &&str) -> bool { 
    let mut xy = field.split(":");
    let x = xy.next().unwrap();
    let y = xy.next().unwrap();
    match x {
        "byr" => is_in_range(y, 1920..=2002),
        "iyr" => is_in_range(y, 2010..=2020),
        "eyr" => is_in_range(y, 2010..=2030),
        "hgt" => is_in_range_height(y, 150..=193, "cm") || is_in_range_height(y, 59..=76, "in"),
        "hcl" => y
            .strip_prefix("#")
            .map_or(false, |rest| rest.chars().all(|c| c.is_ascii_hexdigit())),
        "ecl" => matches!(y, "amb" | "blu" | "brn" | "gry" | "grn" | "hzl" | "oth"),
        "pid" => y.len() == 9 && y.chars().all(|c| c.is_ascii_digit()),
        _ => false,
    }
}


fn is_in_range(s: &str, range: RangeInclusive<u16>) -> bool {
    s.parse().map_or(false, |n: u16| range.contains(&n))
}

/*Diffrent range function built for the height category, as it needs a suffix (it can be both in cm or in.)*/

fn is_in_range_height(s: &str, range: RangeInclusive<u16>, suffix: &str) -> bool {
    s.strip_suffix(suffix)
        .map_or(false, |rest| is_in_range(rest, range))
}
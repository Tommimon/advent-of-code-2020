# Part Two Solution (below you can find example five solution)
We want to find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at the subsequent minute given by his position in the list of bus IDs.

| ID (Bus ID) | Delta Time |
|   :----:    |   :----:   |
| 19          | 0          |
| 41          | 9          |
| 523         | 19         |
| 17          | 36         |
| 13          | 37         |
| 29          | 48         |
| 853         | 50         |
| 37          | 56         |
| 23          | 73         |


My input for part 2 is:
```
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,x,x,x,x,x,x,x,x,x,x,29,x,853,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23
```

***

## Apply the condition to a pair of busses at a time and find all the times t (for each pair) where the condition is satisfied. 
Do this on 9 pairs so that every number is used exactly two times.

ID 19 with ID 41
```
solve t = 0 (mod 19), t+9 = 0 (mod 41)
--> t = 779n + 114
```
ID 41 with ID 523
```
solve t+9 = 0 (mod 41), t+19 = 0 (mod 523)
--> t = 21433n + 20901
```
ID 523 with ID 17
```
solve t+19 = 0 (mod 523), t+36 = 0 (mod 17)
--> t = 8891n + 8872
```
ID 17 with ID 13
```
solve t+36 = 0 (mod 17), t+37 = 0 (mod 13)
--> t = 221n + 15
```
ID 13 with ID 29
```
solve t+37 = 0 (mod 13), t+48 = 0 (mod 29)
--> t = 377n + 184
```
ID 29 with ID 853
```
solve t+48 = 0 (mod 29), t+50 = 0 (mod 853)
--> t = 24737n + 4215
```
ID  853 with ID 37
```
solve t+50 = 0 (mod 853), t+56 = 0 (mod 37)
--> t = 31561n + 28952
```
ID 37 with ID 23
```
solve t+56 = 0 (mod 37), t+73 = 0 (mod 23)
--> t = 851n + 203
```
ID 19 with ID 23
```
solve t = 0 (mod 19), t+73 = 0 (mod 23)
--> t = 437n + 19
```
!!! In all these equations **n is a integer number**, but we actually know it must be positive since time can not be negative.

## We want to find the timestamps ```t``` where all these conditions are met. So I put all the ```t``` equal to each other in a system.
(I changed all the ```n``` with other names because they are indipendent between all these equations)

```
779a+114 == 21443b+20901
21443b+20901 == 8891c+8872
8891c+8872 == 221d+15
221d+15 == 377e+184
377e+184 == 24737f+4215
24737f+4215 == 31561g+28952
31561g+28952 == 851h+203
851h+203 == 437i+19
```

Which then becomes

```
779 a -21443 b  = 20787
21443 b -8891 c = -12029
8891 c - 221 d = -8857
221 d - 377 e = 169
377 e -24737 f  = 4031
24737 f - 31561 g = 24737
31561 g - 851 h = -28749
851 h - 437 i = -184
```

## Now we have to solve this system remembering that all our variables are positive integers.
It took me very long to find a way to solve this system given that the variables must be integers. I tried many websites and libraries, but none seemed to work.

Then, after a couple hours, I found what I was looking for: "Solving a system of linear diophantine equations using the Hermite normal form of an integer matrix via the Havas-Majewski-Matthews LLL-based algorithm" at http://www.numbertheory.org/php/axb.html

The system has 8 equations in 9 variables so the input is:
```
m = 8

n = 9

m × (n+1) augmented matrix:
779 -21443 0 0 0 0 0 0 0 20787
0 21443 -8891 0 0 0 0 0 0 -12029
0 0 8891 -221 0 0 0 0 0 -8857
0 0 0 221 -377 0 0 0 0 169
0 0 0 0 377 -24737 0 0 0 4031
0 0 0 0 0 24737 -31561 0 0 24737
0 0 0 0 0 0 31561 -851 0 -28749
0 0 0 0 0 0 0 851 -437 -184
```

The Havas-Majewski-Matthews LLL-based algorithm does the magic.
Now just take the shortest solution vector:
```
V = (270363189832, 9821989687, 23688328070, 952999660087, 558654973154, 8514085171, 6673201890, 247488748389, 481951773179) 
```

## Calculate the timestamp
Take ```270363189832``` which is the smallest possible value of the variable ```a``` and calculate the timestamp with the equation found above:

```
t = 779a+114

--> 779 * 270363189832 + 114 = 210612924879242
```

## Solution
```
210612924879242
```

## Considerations
I must study some Number Theory for the future and maybe try first an "intelligent bruteforce" approach (I know that in this puzzle works perfectly - check marcomole00 solution), but luckly this time my Linear Algebra skills were enough to find the answer.



***
----
***

# Same resolution method applied to example five

| ID (Bus ID) | Delta Time |
|   :----:    |   :----:   |
| 1789        | 0          |
| 37          | 1          |
| 47          | 2          |
| 1889        | 3          |

Input for example five is:
```
1789,37,47,1889
```

***

## Apply the condition to a pair of busses at a time and find all the times t (for each pair) where the condition is satisfied. 

ID 67 with ID 37
```
solve t = 0 (mod 1789), t+1= 0 (mod 37)
--> t = 66193 n + 30413
```
ID 37 with ID 59
```
solve t+1 = 0 (mod 37), t+2 = 0 (mod 47)
--> t = 1739 n + 1220
```
ID 59 with ID 1889
```
solve t+2 = 0 (mod 47), t+3 = 0 (mod 1889)
--> t = 88783 n + 39666
```
ID 67 with ID 61
```
solve t = 0 (mod 1789), t+3 = 0 (mod 1889)
--> t = 3379421 n + 2467031
```

## We want to find the timestamps ```t``` where all these conditions are met. So I put all the ```t``` equal to each other in a system.

```
66193 a + 30413 = 1739 b + 1220
1739 b + 1220 = 88783 c + 39666
88783 c + 39666 = 3379421 d + 2467031
```

Which then becomes

```
66193 a - 1739 b = - 29193
1739 b - 88783 c = 38446
88783 c - 3379421 d = 2427365
```

## Now we have to solve this system remembering that all our variables are positive integers.

The system has 3 equations in 4 variables so:
```
m = 3

n = 4

m × (n+1) augmented matrix:
66193 -1739 0 0 -29193
0 1739 -88783 0 38446
0 0 88783 -3379421 2427365
```

Shortest solution vector:
```
V = (18161, 691294, 13540, 355)  
```

## Calculate the timestamp
Take ```18161``` which is the smallest possible value of the variable ```a``` and calculate the timestamp with the equation found above:

```
t = 66193 a + 30413

--> 66193 * 18161 + 30413 = 1202161486
```

## Solution
```
1202161486
```
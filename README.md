# [Advent of Code 2020](https://adventofcode.com/)

<pre>

            |,\/,| |[_' |[_]) |[_]) \\//    // ' |[_]| |[_]) || ((_' '||' |,\/,|  //\\  ((_'
            ||\/|| |[_, ||'\, ||'\,  ||     \\_, |[']| ||'\, || ,_))  ||  ||\/|| //``\\ ,_))



                                                                 ,;7,
                                                               _ ||:|,
                                             _,---,_           )\'  '|
                                           .'_.-.,_ '.         ',')  j
                                          /,'   ___}  \        _/   /
                              .,         ,1  .''  =\ _.''.   ,`';_ |
                            .'  \        (.'T ~, (' ) ',.'  /     ';',
                            \   .\(\O/)_. \ (    _Z-'`>--, .'',      ;
                             \  |   I  _|._>;--'`,-j-'    ;    ',  .'
                            __\_|   _.'.-7 ) `'-' "       (      ;'
                          .'.'_.'|.' .'   \ ',_           .'\   /
                          | |  |.'  /      \   \          l  \ /
                          | _.-'   /        '. ('._   _ ,.'   \i
                        ,--' ---' / k  _.-,.-|__L, '-' ' ()    ;
                         '._     (   ';   (    _-}             |
                          / '     \   ;    ',.__;         ()   /
                         /         |   ;    ; ___._._____.: :-j
                        |           \,__',-' ____: :_____.: :-\
                        |               F :   .  ' '        ,  L
                        ',             J  |   ;             j  |
                          \            |  |    L            |  J
                           ;         .-F  |    ;           J    L
                            \___,---' J'--:    j,---,___   |_   |
                                      |   |'--' L       '--| '-'|
                                       '.,L     |----.__   j.__.'
                                        | '----'   |,   '-'  }
                                        j         / ('-----';
                                       { "---'--;'  }       |
                                       |        |   '.----,.'
                                       ',.__.__.'    |=, _/
                                        |     /      |    '.
                                        |'= -x       L___   '--,
                                        L   __\          '-----'
                                         '.____)
</pre>

## Solved problems

### Edit table
You can edit the local version of the table with the python script `edit_table.py`

To run the script use `python3 edit_table.py` in your terminal

### Table
- Blank spaces are unsolved problems
- `*` if you solved the first part
- `**` if you also solved the second part

| | <a href="https://github.com/riccardo-negri"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/riccardo-negri.png" width="40" height="40"/></a> | <a href="https://github.com/Tommimon"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/Tommimon.png" width="40" height="40"/></a> | <a href="https://github.com/Gonduls"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/Gonduls.png" width="40" height="40"/></a> | <a href="https://github.com/marcomole00"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/marcomole00.png" width="40" height="40"/></a> | <a href="https://github.com/marcoparadina"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/marcoparadina.png" width="40" height="40"/></a> | <a href="https://github.com/mynam3isg00d"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/mynam3isg00d.png" width="40" height="40"/></a> | <a href="https://github.com/IronBlack"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/IronBlack.png" width="40" height="40"/></a> | <a href="https://github.com/SebPelli"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/SebPelli.png" width="40" height="40"/></a> | <a href="https://github.com/Sunriser45"><img src="https://github.com/Tommimon/advent-of-code-2020/blob/master/Assets/Sunriser45.png" width="40" height="40"/></a> |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
| **Day** | <a href="https://github.com/riccardo-negri"><sup><sub>riccardo-negri</sub></sup></a> | <a href="https://github.com/Tommimon"><sup><sub>Tommimon</sub></sup></a> | <a href="https://github.com/Gonduls"><sup><sub>Gonduls</sub></sup></a> | <a href="https://github.com/marcomole00"><sup><sub>marcomole00</sub></sup></a> | <a href="https://github.com/marcoparadina"><sup><sub>marcoparadina</sub></sup></a> | <a href="https://github.com/mynam3isg00d"><sup><sub>mynam3isg00d</sub></sup></a> | <a href="https://github.com/IronBlack"><sup><sub>MatteoBlack</sub></sup></a> | <a href="https://github.com/SebPelli"><sup><sub>SebPelli</sub></sup></a> | <a href="https://github.com/Sunriser45"><sup><sub>Sunriser45</sub></sup></a> |
[1 ][d01] | [**][u01d01] | [**][u02d01] | [**][u03d01] | [**][u04d01] | [**][u05d01] | [**][u06d01] | [**][u07d01] | [**][u08d01] | [**][u09d01] | [  ][u10d01] | [  ][u11d01] | [  ][u12d01] | [  ][u13d01] | [  ][u14d01] | [  ][u15d01] | [  ][u16d01] | [  ][u17d01] | [  ][u18d01] | [  ][u19d01] | [  ][u20d01]
[2 ][d02] | [**][u01d02] | [**][u02d02] | [**][u03d02] | [**][u04d02] | [**][u05d02] | [**][u06d02] | [**][u07d02] | [**][u08d02] | [  ][u09d02] | [  ][u10d02] | [  ][u11d02] | [  ][u12d02] | [  ][u13d02] | [  ][u14d02] | [  ][u15d02] | [  ][u16d02] | [  ][u17d02] | [  ][u18d02] | [  ][u19d02] | [  ][u20d02]
[3 ][d03] | [**][u01d03] | [**][u02d03] | [**][u03d03] | [**][u04d03] | [**][u05d03] | [**][u06d03] | [**][u07d03] | [**][u08d03] | [  ][u09d03] | [  ][u10d03] | [  ][u11d03] | [  ][u12d03] | [  ][u13d03] | [  ][u14d03] | [  ][u15d03] | [  ][u16d03] | [  ][u17d03] | [  ][u18d03] | [  ][u19d03] | [  ][u20d03]
[4 ][d04] | [**][u01d04] | [**][u02d04] | [**][u03d04] | [**][u04d04] | [**][u05d04] | [**][u06d04] | [**][u07d04] | [**][u08d04] | [  ][u09d04] | [  ][u10d04] | [  ][u11d04] | [  ][u12d04] | [  ][u13d04] | [  ][u14d04] | [  ][u15d04] | [  ][u16d04] | [  ][u17d04] | [  ][u18d04] | [  ][u19d04] | [  ][u20d04]
[5 ][d05] | [**][u01d05] | [**][u02d05] | [**][u03d05] | [**][u04d05] | [**][u05d05] | [**][u06d05] | [**][u07d05] | [**][u08d05] | [  ][u09d05] | [  ][u10d05] | [  ][u11d05] | [  ][u12d05] | [  ][u13d05] | [  ][u14d05] | [  ][u15d05] | [  ][u16d05] | [  ][u17d05] | [  ][u18d05] | [  ][u19d05] | [  ][u20d05]
[6 ][d06] | [**][u01d06] | [**][u02d06] | [**][u03d06] | [**][u04d06] | [**][u05d06] | [**][u06d06] | [**][u07d06] | [**][u08d06] | [  ][u09d06] | [  ][u10d06] | [  ][u11d06] | [  ][u12d06] | [  ][u13d06] | [  ][u14d06] | [  ][u15d06] | [  ][u16d06] | [  ][u17d06] | [  ][u18d06] | [  ][u19d06] | [  ][u20d06]
[7 ][d07] | [**][u01d07] | [**][u02d07] | [**][u03d07] | [**][u04d07] | [  ][u05d07] | [**][u06d07] | [**][u07d07] | [  ][u08d07] | [  ][u09d07] | [  ][u10d07] | [  ][u11d07] | [  ][u12d07] | [  ][u13d07] | [  ][u14d07] | [  ][u15d07] | [  ][u16d07] | [  ][u17d07] | [  ][u18d07] | [  ][u19d07] | [  ][u20d07]
[8 ][d08] | [**][u01d08] | [**][u02d08] | [**][u03d08] | [**][u04d08] | [**][u05d08] | [**][u06d08] | [**][u07d08] | [  ][u08d08] | [  ][u09d08] | [  ][u10d08] | [  ][u11d08] | [  ][u12d08] | [  ][u13d08] | [  ][u14d08] | [  ][u15d08] | [  ][u16d08] | [  ][u17d08] | [  ][u18d08] | [  ][u19d08] | [  ][u20d08]
[9 ][d09] | [**][u01d09] | [**][u02d09] | [**][u03d09] | [**][u04d09] | [**][u05d09] | [**][u06d09] | [**][u07d09] | [  ][u08d09] | [  ][u09d09] | [  ][u10d09] | [  ][u11d09] | [  ][u12d09] | [  ][u13d09] | [  ][u14d09] | [  ][u15d09] | [  ][u16d09] | [  ][u17d09] | [  ][u18d09] | [  ][u19d09] | [  ][u20d09]
[10][d10] | [**][u01d10] | [**][u02d10] | [**][u03d10] | [* ][u04d10] | [  ][u05d10] | [**][u06d10] | [**][u07d10] | [  ][u08d10] | [  ][u09d10] | [  ][u10d10] | [  ][u11d10] | [  ][u12d10] | [  ][u13d10] | [  ][u14d10] | [  ][u15d10] | [  ][u16d10] | [  ][u17d10] | [  ][u18d10] | [  ][u19d10] | [  ][u20d10]
[11][d11] | [**][u01d11] | [**][u02d11] | [**][u03d11] | [**][u04d11] | [  ][u05d11] | [**][u06d11] | [**][u07d11] | [  ][u08d11] | [  ][u09d11] | [  ][u10d11] | [  ][u11d11] | [  ][u12d11] | [  ][u13d11] | [  ][u14d11] | [  ][u15d11] | [  ][u16d11] | [  ][u17d11] | [  ][u18d11] | [  ][u19d11] | [  ][u20d11]
[12][d12] | [**][u01d12] | [**][u02d12] | [**][u03d12] | [**][u04d12] | [  ][u05d12] | [**][u06d12] | [**][u07d12] | [  ][u08d12] | [  ][u09d12] | [  ][u10d12] | [  ][u11d12] | [  ][u12d12] | [  ][u13d12] | [  ][u14d12] | [  ][u15d12] | [  ][u16d12] | [  ][u17d12] | [  ][u18d12] | [  ][u19d12] | [  ][u20d12]
[13][d13] | [**][u01d13] | [**][u02d13] | [**][u03d13] | [**][u04d13] | [  ][u05d13] | [  ][u06d13] | [**][u07d13] | [  ][u08d13] | [  ][u09d13] | [  ][u10d13] | [  ][u11d13] | [  ][u12d13] | [  ][u13d13] | [  ][u14d13] | [  ][u15d13] | [  ][u16d13] | [  ][u17d13] | [  ][u18d13] | [  ][u19d13] | [  ][u20d13]
[14][d14] | [**][u01d14] | [**][u02d14] | [**][u03d14] | [**][u04d14] | [  ][u05d14] | [**][u06d14] | [*][u07d14] | [  ][u08d14] | [  ][u09d14] | [  ][u10d14] | [  ][u11d14] | [  ][u12d14] | [  ][u13d14] | [  ][u14d14] | [  ][u15d14] | [  ][u16d14] | [  ][u17d14] | [  ][u18d14] | [  ][u19d14] | [  ][u20d14]
[15][d15] | [**][u01d15] | [**][u02d15] | [**][u03d15] | [**][u04d15] | [  ][u05d15] | [**][u06d15] | [  ][u07d15] | [  ][u08d15] | [  ][u09d15] | [  ][u10d15] | [  ][u11d15] | [  ][u12d15] | [  ][u13d15] | [  ][u14d15] | [  ][u15d15] | [  ][u16d15] | [  ][u17d15] | [  ][u18d15] | [  ][u19d15] | [  ][u20d15]
[16][d16] | [**][u01d16] | [**][u02d16] | [**][u03d16] | [**][u04d16] | [  ][u05d16] | [  ][u06d16] | [**][u07d16] | [  ][u08d16] | [  ][u09d16] | [  ][u10d16] | [  ][u11d16] | [  ][u12d16] | [  ][u13d16] | [  ][u14d16] | [  ][u15d16] | [  ][u16d16] | [  ][u17d16] | [  ][u18d16] | [  ][u19d16] | [  ][u20d16]
[17][d17] | [**][u01d17] | [**][u02d17] | [**][u03d17] | [**][u04d17] | [  ][u05d17] | [**][u06d17] | [**][u07d17] | [  ][u08d17] | [  ][u09d17] | [  ][u10d17] | [  ][u11d17] | [  ][u12d17] | [  ][u13d17] | [  ][u14d17] | [  ][u15d17] | [  ][u16d17] | [  ][u17d17] | [  ][u18d17] | [  ][u19d17] | [  ][u20d17]
[18][d18] | [**][u01d18] | [**][u02d18] | [**][u03d18] | [  ][u04d18] | [  ][u05d18] | [  ][u06d18] | [**][u07d18] | [  ][u08d18] | [  ][u09d18] | [  ][u10d18] | [  ][u11d18] | [  ][u12d18] | [  ][u13d18] | [  ][u14d18] | [  ][u15d18] | [  ][u16d18] | [  ][u17d18] | [  ][u18d18] | [  ][u19d18] | [  ][u20d18]
[19][d19] | [**][u01d19] | [**][u02d19] | [**][u03d19] | [  ][u04d19] | [  ][u05d19] | [  ][u06d19] | [  ][u07d19] | [  ][u08d19] | [  ][u09d19] | [  ][u10d19] | [  ][u11d19] | [  ][u12d19] | [  ][u13d19] | [  ][u14d19] | [  ][u15d19] | [  ][u16d19] | [  ][u17d19] | [  ][u18d19] | [  ][u19d19] | [  ][u20d19]
[20][d20] | [**][u01d20] | [**][u02d20] | [  ][u03d20] | [  ][u04d20] | [  ][u05d20] | [  ][u06d20] | [  ][u07d20] | [  ][u08d20] | [  ][u09d20] | [  ][u10d20] | [  ][u11d20] | [  ][u12d20] | [  ][u13d20] | [  ][u14d20] | [  ][u15d20] | [  ][u16d20] | [  ][u17d20] | [  ][u18d20] | [  ][u19d20] | [  ][u20d20]
[21][d21] | [**][u01d21] | [**][u02d21] | [  ][u03d21] | [  ][u04d21] | [  ][u05d21] | [  ][u06d21] | [  ][u07d21] | [  ][u08d21] | [  ][u09d21] | [  ][u10d21] | [  ][u11d21] | [  ][u12d21] | [  ][u13d21] | [  ][u14d21] | [  ][u15d21] | [  ][u16d21] | [  ][u17d21] | [  ][u18d21] | [  ][u19d21] | [  ][u20d21]
[22][d22] | [  ][u01d22] | [  ][u02d22] | [  ][u03d22] | [  ][u04d22] | [  ][u05d22] | [  ][u06d22] | [  ][u07d22] | [  ][u08d22] | [  ][u09d22] | [  ][u10d22] | [  ][u11d22] | [  ][u12d22] | [  ][u13d22] | [  ][u14d22] | [  ][u15d22] | [  ][u16d22] | [  ][u17d22] | [  ][u18d22] | [  ][u19d22] | [  ][u20d22]
[23][d23] | [  ][u01d23] | [  ][u02d23] | [  ][u03d23] | [  ][u04d23] | [  ][u05d23] | [  ][u06d23] | [  ][u07d23] | [  ][u08d23] | [  ][u09d23] | [  ][u10d23] | [  ][u11d23] | [  ][u12d23] | [  ][u13d23] | [  ][u14d23] | [  ][u15d23] | [  ][u16d23] | [  ][u17d23] | [  ][u18d23] | [  ][u19d23] | [  ][u20d23]
[24][d24] | [  ][u01d24] | [  ][u02d24] | [  ][u03d24] | [  ][u04d24] | [  ][u05d24] | [  ][u06d24] | [  ][u07d24] | [  ][u08d24] | [  ][u09d24] | [  ][u10d24] | [  ][u11d24] | [  ][u12d24] | [  ][u13d24] | [  ][u14d24] | [  ][u15d24] | [  ][u16d24] | [  ][u17d24] | [  ][u18d24] | [  ][u19d24] | [  ][u20d24]
[25][d25] | [  ][u01d25] | [  ][u02d25] | [  ][u03d25] | [  ][u04d25] | [  ][u05d25] | [  ][u06d25] | [  ][u07d25] | [  ][u08d25] | [  ][u09d25] | [  ][u10d25] | [  ][u11d25] | [  ][u12d25] | [  ][u13d25] | [  ][u14d25] | [  ][u15d25] | [  ][u16d25] | [  ][u17d25] | [  ][u18d25] | [  ][u19d25] | [  ][u20d25]


[d01]: https://adventofcode.com/2020/day/1
[d02]: https://adventofcode.com/2020/day/2
[d03]: https://adventofcode.com/2020/day/3
[d04]: https://adventofcode.com/2020/day/4
[d05]: https://adventofcode.com/2020/day/5
[d06]: https://adventofcode.com/2020/day/6
[d07]: https://adventofcode.com/2020/day/7
[d08]: https://adventofcode.com/2020/day/8
[d09]: https://adventofcode.com/2020/day/9
[d10]: https://adventofcode.com/2020/day/10
[d11]: https://adventofcode.com/2020/day/11
[d12]: https://adventofcode.com/2020/day/12
[d13]: https://adventofcode.com/2020/day/13
[d14]: https://adventofcode.com/2020/day/14
[d15]: https://adventofcode.com/2020/day/15
[d16]: https://adventofcode.com/2020/day/16
[d17]: https://adventofcode.com/2020/day/17
[d18]: https://adventofcode.com/2020/day/18
[d19]: https://adventofcode.com/2020/day/19
[d20]: https://adventofcode.com/2020/day/20
[d21]: https://adventofcode.com/2020/day/21
[d22]: https://adventofcode.com/2020/day/22
[d23]: https://adventofcode.com/2020/day/23
[d24]: https://adventofcode.com/2020/day/24
[d25]: https://adventofcode.com/2020/day/25

[u01d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/01
[u01d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/02
[u01d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/03
[u01d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/04
[u01d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/05
[u01d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/06
[u01d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/07
[u01d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/08
[u01d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/09
[u01d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/10
[u01d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/11
[u01d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/12
[u01d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/13
[u01d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/14
[u01d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/15
[u01d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/16
[u01d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/17
[u01d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/18
[u01d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/19
[u01d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/20
[u01d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/21
[u01d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/22
[u01d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/23
[u01d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/24
[u01d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/riccardo-negri/25
[u02d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/01
[u02d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/02
[u02d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/03
[u02d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/04
[u02d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/05
[u02d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/06
[u02d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/07
[u02d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/08
[u02d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/09
[u02d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/10
[u02d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/11
[u02d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/12
[u02d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/13
[u02d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/14
[u02d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/15
[u02d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/16
[u02d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/17
[u02d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/18
[u02d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/19
[u02d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/20
[u02d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/21
[u02d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/22
[u02d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/23
[u02d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/24
[u02d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Tommimon/25
[u03d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/01
[u03d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/02
[u03d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/03
[u03d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/04
[u03d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/05
[u03d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/06
[u03d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/07
[u03d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/08
[u03d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/09
[u03d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/10
[u03d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/11
[u03d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/12
[u03d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/13
[u03d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/14
[u03d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/15
[u03d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/16
[u03d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/17
[u03d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/18
[u03d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/19
[u03d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/20
[u03d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/21
[u03d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/22
[u03d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/23
[u03d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/24
[u03d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Gonduls/25
[u04d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/01
[u04d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/02
[u04d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/03
[u04d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/04
[u04d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/05
[u04d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/06
[u04d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/07
[u04d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/08
[u04d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/09
[u04d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/10
[u04d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/11
[u04d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/12
[u04d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/13
[u04d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/14
[u04d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/15
[u04d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/16
[u04d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/17
[u04d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/18
[u04d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/19
[u04d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/20
[u04d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/21
[u04d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/22
[u04d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/23
[u04d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/24
[u04d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcomole00/25
[u05d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/01
[u05d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/02
[u05d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/03
[u05d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/04
[u05d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/05
[u05d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/06
[u05d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/07
[u05d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/08
[u05d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/09
[u05d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/10
[u05d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/11
[u05d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/12
[u05d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/13
[u05d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/14
[u05d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/15
[u05d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/16
[u05d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/17
[u05d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/18
[u05d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/19
[u05d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/20
[u05d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/21
[u05d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/22
[u05d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/23
[u05d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/24
[u05d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/marcoparadina/25
[u06d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/01
[u06d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/02
[u06d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/03
[u06d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/04
[u06d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/05
[u06d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/06
[u06d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/07
[u06d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/08
[u06d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/09
[u06d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/10
[u06d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/11
[u06d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/12
[u06d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/13
[u06d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/14
[u06d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/15
[u06d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/16
[u06d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/17
[u06d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/18
[u06d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/19
[u06d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/20
[u06d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/21
[u06d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/22
[u06d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/23
[u06d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/24
[u06d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/mynam3isg00d/25
[u07d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/01
[u07d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/02
[u07d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/03
[u07d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/04
[u07d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/05
[u07d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/06
[u07d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/07
[u07d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/08
[u07d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/09
[u07d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/10
[u07d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/11
[u07d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/12
[u07d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/13
[u07d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/14
[u07d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/15
[u07d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/16
[u07d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/17
[u07d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/18
[u07d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/19
[u07d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/20
[u07d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/21
[u07d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/22
[u07d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/23
[u07d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/24
[u07d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/MatteoBlack/25
[u08d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/01
[u08d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/02
[u08d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/03
[u08d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/04
[u08d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/05
[u08d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/06
[u08d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/07
[u08d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/08
[u08d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/09
[u08d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/10
[u08d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/11
[u08d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/12
[u08d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/13
[u08d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/14
[u08d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/15
[u08d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/16
[u08d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/17
[u08d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/18
[u08d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/19
[u08d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/20
[u08d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/21
[u08d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/22
[u08d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/23
[u08d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/24
[u08d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/SebPelli/25
[u09d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/01
[u09d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/02
[u09d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/03
[u09d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/04
[u09d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/05
[u09d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/06
[u09d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/07
[u09d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/08
[u09d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/09
[u09d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/10
[u09d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/11
[u09d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/12
[u09d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/13
[u09d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/14
[u09d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/15
[u09d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/16
[u09d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/17
[u09d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/18
[u09d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/19
[u09d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/20
[u09d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/21
[u09d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/22
[u09d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/23
[u09d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/24
[u09d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/Sunriser45/25
[u10d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/01
[u10d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/02
[u10d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/03
[u10d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/04
[u10d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/05
[u10d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/06
[u10d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/07
[u10d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/08
[u10d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/09
[u10d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/10
[u10d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/11
[u10d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/12
[u10d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/13
[u10d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/14
[u10d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/15
[u10d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/16
[u10d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/17
[u10d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/18
[u10d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/19
[u10d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/20
[u10d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/21
[u10d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/22
[u10d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/23
[u10d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/24
[u10d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User10/25
[u11d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/01
[u11d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/02
[u11d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/03
[u11d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/04
[u11d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/05
[u11d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/06
[u11d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/07
[u11d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/08
[u11d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/09
[u11d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/10
[u11d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/11
[u11d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/12
[u11d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/13
[u11d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/14
[u11d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/15
[u11d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/16
[u11d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/17
[u11d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/18
[u11d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/19
[u11d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/20
[u11d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/21
[u11d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/22
[u11d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/23
[u11d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/24
[u11d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User11/25
[u12d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/01
[u12d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/02
[u12d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/03
[u12d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/04
[u12d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/05
[u12d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/06
[u12d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/07
[u12d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/08
[u12d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/09
[u12d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/10
[u12d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/11
[u12d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/12
[u12d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/13
[u12d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/14
[u12d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/15
[u12d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/16
[u12d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/17
[u12d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/18
[u12d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/19
[u12d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/20
[u12d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/21
[u12d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/22
[u12d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/23
[u12d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/24
[u12d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User12/25
[u13d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/01
[u13d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/02
[u13d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/03
[u13d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/04
[u13d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/05
[u13d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/06
[u13d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/07
[u13d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/08
[u13d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/09
[u13d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/10
[u13d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/11
[u13d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/12
[u13d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/13
[u13d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/14
[u13d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/15
[u13d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/16
[u13d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/17
[u13d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/18
[u13d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/19
[u13d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/20
[u13d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/21
[u13d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/22
[u13d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/23
[u13d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/24
[u13d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User13/25
[u14d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/01
[u14d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/02
[u14d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/03
[u14d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/04
[u14d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/05
[u14d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/06
[u14d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/07
[u14d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/08
[u14d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/09
[u14d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/10
[u14d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/11
[u14d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/12
[u14d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/13
[u14d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/14
[u14d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/15
[u14d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/16
[u14d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/17
[u14d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/18
[u14d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/19
[u14d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/20
[u14d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/21
[u14d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/22
[u14d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/23
[u14d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/24
[u14d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User14/25
[u15d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/01
[u15d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/02
[u15d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/03
[u15d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/04
[u15d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/05
[u15d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/06
[u15d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/07
[u15d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/08
[u15d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/09
[u15d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/10
[u15d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/11
[u15d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/12
[u15d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/13
[u15d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/14
[u15d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/15
[u15d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/16
[u15d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/17
[u15d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/18
[u15d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/19
[u15d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/20
[u15d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/21
[u15d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/22
[u15d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/23
[u15d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/24
[u15d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User15/25
[u16d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/01
[u16d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/02
[u16d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/03
[u16d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/04
[u16d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/05
[u16d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/06
[u16d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/07
[u16d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/08
[u16d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/09
[u16d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/10
[u16d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/11
[u16d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/12
[u16d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/13
[u16d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/14
[u16d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/15
[u16d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/16
[u16d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/17
[u16d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/18
[u16d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/19
[u16d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/20
[u16d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/21
[u16d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/22
[u16d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/23
[u16d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/24
[u16d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User16/25
[u17d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/01
[u17d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/02
[u17d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/03
[u17d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/04
[u17d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/05
[u17d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/06
[u17d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/07
[u17d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/08
[u17d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/09
[u17d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/10
[u17d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/11
[u17d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/12
[u17d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/13
[u17d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/14
[u17d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/15
[u17d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/16
[u17d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/17
[u17d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/18
[u17d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/19
[u17d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/20
[u17d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/21
[u17d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/22
[u17d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/23
[u17d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/24
[u17d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User17/25
[u18d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/01
[u18d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/02
[u18d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/03
[u18d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/04
[u18d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/05
[u18d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/06
[u18d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/07
[u18d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/08
[u18d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/09
[u18d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/10
[u18d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/11
[u18d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/12
[u18d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/13
[u18d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/14
[u18d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/15
[u18d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/16
[u18d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/17
[u18d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/18
[u18d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/19
[u18d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/20
[u18d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/21
[u18d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/22
[u18d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/23
[u18d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/24
[u18d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User18/25
[u19d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/01
[u19d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/02
[u19d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/03
[u19d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/04
[u19d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/05
[u19d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/06
[u19d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/07
[u19d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/08
[u19d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/09
[u19d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/10
[u19d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/11
[u19d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/12
[u19d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/13
[u19d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/14
[u19d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/15
[u19d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/16
[u19d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/17
[u19d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/18
[u19d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/19
[u19d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/20
[u19d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/21
[u19d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/22
[u19d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/23
[u19d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/24
[u19d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User19/25
[u20d01]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/01
[u20d02]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/02
[u20d03]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/03
[u20d04]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/04
[u20d05]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/05
[u20d06]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/06
[u20d07]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/07
[u20d08]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/08
[u20d09]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/09
[u20d10]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/10
[u20d11]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/11
[u20d12]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/12
[u20d13]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/13
[u20d14]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/14
[u20d15]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/15
[u20d16]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/16
[u20d17]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/17
[u20d18]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/18
[u20d19]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/19
[u20d20]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/20
[u20d21]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/21
[u20d22]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/22
[u20d23]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/23
[u20d24]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/24
[u20d25]: https://github.com/Tommimon/advent-of-code-2020/tree/master/User20/25

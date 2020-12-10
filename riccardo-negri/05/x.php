<?php

// Day 5 solution of Advent Of Code 2020 by Riccardo Negri
// First part answer: 991
// Second part answer: 534

const COL_BITS = 3; 
const ROW_BITS = 7; 

$index = 0;
if ($file = fopen("input.txt", "r")) {
    while(!feof($file)) {
        $line = fgets($file);
        $line = str_replace('F', '0', $line);
        $line = str_replace('B', '1', $line);
        $line = str_replace('L', '0', $line);
        $line = str_replace('R', '1', $line);
        $row = bindec(substr($line,0,7));
        $column = bindec(substr($line,7,10));
        $ID = $row * 8 + $column;
        $SeatsInfo[0][$index] = $row;
        $SeatsInfo[1][$index] = $column;
        $SeatsInfo[2][$index] = $ID;	
        $index++;
    }
    fclose($file);
}

echo "Max ID (First part answer): ".max($SeatsInfo[2])."\n";

foreach (range(0, 2**(COL_BITS)-1) as $column) {
    foreach (range(0, 2**(ROW_BITS)-1) as $row) {
        $ID = $row * 8 + $column;
        if (!in_array($ID, $SeatsInfo[2])) {
        	if (in_array(($ID-1), $SeatsInfo[2]) and in_array(($ID+1), $SeatsInfo[2])) {
        		$myID =  $ID;
        	}
        }
    }
}

echo "My ID (Second part answer): ".$myID."\n";

?>
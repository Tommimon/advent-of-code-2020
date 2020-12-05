<?php

// Day 4 solution of Advent Of Code 2020 by Riccardo Negri
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

//echo "Max ID (First part answer): ".max($SeatsInfo[2])."\n";

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

//echo "My ID (Second part answer): ".$myID."\n";

?>
<html>
<body>
<h1>Welcome to the plane seats checking system</h1>
<h2>Advent of Code 2020 edition</h2>
<table>
<?php
foreach (range(-1, 2**(ROW_BITS)-1) as $row) {

    echo "<tr>";
    if ($row != -1) {
        echo "<td><p>".$row."</p></td>";
    }
    else {
        echo "<td><div class=\"seat\"></div></td>";
    }
    
    foreach (range(0, 2**(COL_BITS)-1) as $column) {
        if ($row == -1) {
             echo "<td><p>".$column."</p></td>";
        }
        else {
            $ID = $row * 8 + $column;
            if (in_array($ID, $SeatsInfo[2])) {
                $class = "class=\"seat occupied\"";
            }
            elseif ($ID == $myID) {
                $class = "class=\"seat myseat\"";
            }
            else {
                $class = "class=\"seat notexist\"";
            }
            //$class = "class=\"myseat\"";
            echo "<td><div ".$class."></div></td>";
        }
    }
    echo "</tr>";
}
?>
</table>
<style>
.seat {
    padding: 7px;
}
.occupied {
    background: red;
    
}
.myseat {
    background: green;
}
.notexist {
    background: #cacaca;
}
</style>
</body>
</html> 
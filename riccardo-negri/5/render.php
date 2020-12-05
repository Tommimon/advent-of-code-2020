<?php

// Day 5 of Advent Of Code 2020 Render by Riccardo Negri

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

?>
<html>
<?php
echo "<link rel='stylesheet' type='text/css' href='style.css' />";
?>
<body>
<h1>Welcome to the plane seats checking system</h1>
<h2>Advent of Code 2020 edition</h2>
<table>
<?php
foreach (range(-1, 2**(ROW_BITS)-1) as $row) {
    if ($row % 32 == 0 and $row != 0) {
        echo "<tr><td><div class=\"seat\"></div></td></tr>
";
    }
    echo "<tr>";
    if ($row != -1) {
        echo "<td><p>".$row."</p></td>";
    }
    else {
        echo "<td><div class=\"seat\"></div></td>";
    }

    foreach (range(0, 2**(COL_BITS)-1) as $column) {
        if ($column == 3 or $column == 5) {
            echo "<td><div class=\"lane\"></div></td>";
        }

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
            echo "<td><div ".$class."></div></td>";
        }
    }
    echo "</tr>
";
}
?>
</table>
</body>
</html> 
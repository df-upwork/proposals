<?php
$ts = '<path to Tesseract>/tesseract.exe';
$png = '<path to PNG>/%03d.png';
$txt= '<path to TXT>';
for ($i = 1; $i <= $pageCount; $i++) {
    $inFile  = sprintf($png, $i);
    $outFile = sprintf($txt, $i);
    $cmd = "\"$ts\" \"$inFile\" \"$outFile\" -l eng --dpi 300 --psm 3";
    exec($cmd, $output, $returnCode);
}
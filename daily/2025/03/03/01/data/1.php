<?php
$gs = '<path to Ghostscript>/bin/gswin64.exe';
$pdf = '<path to a folder containing the input PDF file>/document.pdf';
$pngFolder  = '<path to a folder with the output PNG files>';
$pngBaseName = '%03d.png';
exec(sprintf(
    '"%s" -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 ' .
    '-dTextAlphaBits=4 -dGraphicsAlphaBits=4 ' .
    '-sOutputFile="%s\\%s" "%s"',
    $gs,
    $pngFolder,
    $pngBaseName,
    $pdf
), $output, $returnCode);

$ts = '<path to Tesseract>/tesseract.exe';
$txtFolder = '<path to a folder with the output text files>';
$txtBaseName = '%03d';
$pageCount = count(glob($pngFolder . '/*.png'));
for ($i = 1; $i <= $pageCount; $i++) {
    exec(sprintf(
        '"%s" "%s" "%s" -l eng --dpi 300 --psm 3',
        $ts,
        sprintf($pngFolder . '/' . $pngBaseName , $i),
        sprintf($txtFolder . '/' . $txtBaseName, $i)
    ), $output, $returnCode);
}

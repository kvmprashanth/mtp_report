set term postscript eps enhanced monochrome 20 dashed dashlength 1 lw 2
set output "throughput.eps"

set style data histogram
set style histogram cluster gap 1 errorbars

set style fill solid border rgb "black"

set xrange [-0.5:2.5]
set yrange [0:8000]
set datafile separator ","

set key font ",12"
set xtics font ",16"
set ytics font ",20"
set ylabel font ",20"
set xlabel font ",20"
set xlabel "Cache allotment"
set ylabel "Application throughput (ops)"
set ytic auto
set boxwidth 1 relative

plot 'data.out' using 2:3:xtic(1) title col(2) fillstyle pattern 12

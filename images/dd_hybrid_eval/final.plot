set term postscript eps enhanced monochrome 20 dashed dashlength 1 lw 2
set output "throughput.eps"

set style data histogram
set style histogram cluster gap 1 errorbars

set style fill solid border rgb "black"
set auto x
set xrange [0.5:9.5]
set yrange [3000:12000]
set key font ",18"
set xtics font ",20"
set ytics font ",20"
set ylabel font ",20"
set xlabel font ",20"
set ylabel "Application throughput (ops/s)"
set xlabel "Cache allocation ratios (Memory : SSD)"  
set ytic auto
set boxwidth 1 relative
set xtics ("8:0" 1, "7:1" 2, "6:2" 3, "5:3" 4, "4:4" 5, "3:5" 6, "2:6" 7, "1:7" 8, "0:8" 9)
#set key on box at 8.2,800

plot  	 'redis.dat' using 1:2 with lines title 'Webserver' lw 3 lc rgb "blue"
#!/bin/sh

echo 00c0 | xxd -r -p > addr.dat
cat addr.dat 01-input.txt > 01-input.prg
petcat -w2 -o 01-1.prg 01-1.bas
c1541 -format day1,01 d64 01.d64 -attach 01.d64 -write 01-1.prg day1 -write 01-input.prg data1
x64 01.d64
rm addr.dat 01-input.prg 01-1.prg 01.d64

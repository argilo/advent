#!/bin/sh

set -e

xxd -i 18-input.txt > 18-input.h
cl65 18-1.c
x64 18-1
rm 18-1 18-1.o 18-input.h

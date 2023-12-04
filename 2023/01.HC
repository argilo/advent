I64 size;
U8 *data = FileRead("Input1.TXT", &size);

I64 i = 0;
I64 sum = 0;
I64 first = -1;
I64 last;
do {
    if (data[i] == '\n') {
        sum += (first * 10) + last;
        first = -1;
    }
    if ((data[i] >= '0') && (data[i] <= '9')) {
        if (first == -1)
            first = data[i] - '0';
        last = data[i] - '0';
    }
} while (++i < size);

Print("Part 1: %d\n", sum);


U8 *words[10] = {
    "", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
};

i = 0;
sum = 0;
do {
    if (data[i] == '\n') {
        sum += (first * 10) + last;
        first = -1;
    }
    if ((data[i] >= '0') && (data[i] <= '9')) {
        if (first == -1)
            first = data[i] - '0';
        last = data[i] - '0';
    }
    I64 n;
    for (n = 1; n < 10; n++) {
        if(MemCmp(&data[i], words[n], StrLen(words[n])) == 0) {
            if (first == -1)
                first = n;
            last = n;
        }
    }
} while (++i < size);

Print("Part 2: %d\n", sum);

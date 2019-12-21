reg2 = 0

seen = set()

while True:
    reg1 = reg2 | 0x10000
    reg2 = 1250634

    while True:
        reg2 = ((reg2 + (reg1 & 0xff)) * 65899) & 0xffffff

        if reg1 < 256:
            if len(seen) == 0:
                print(reg2)
            if reg2 not in seen:
                last = reg2
                seen.add(reg2)
            else:
                print(last)
                exit(0)
            break

        reg1 >>= 8

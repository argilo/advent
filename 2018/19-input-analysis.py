reg0 = 0
reg3 = 974

for reg4 in range(1, reg3+1):
    for reg5 in range(1, reg3+1):
        if reg4 * reg5 == reg3:
            reg0 += reg4

print(reg0)

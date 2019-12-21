#include <stdio.h>
#include <string.h>

#include "18-input.h"

void main(void)
{
	static unsigned char curr[52][52];
	static unsigned char next[52][52];
	int i, r, c, rOff, cOff, trees, lumberyards;

	memset(curr, 0, 52*52);
	memset(next, 0, 52*52);

	for (r = 0; r < 50; r++) {
		for (c = 0; c < 50; c++) {
			curr[r+1][c+1] = __18_input_txt[r*51+c];
		}
	}

	for (i = 0; i < 10; i++) {
		for (r = 0; r < 50; r++) {
			for (c = 0; c < 50; c++) {
				trees = 0;
				lumberyards = 0;
				for (rOff = 0; rOff < 3; rOff++) {
					for (cOff = 0; cOff < 3; cOff++) {
						if (rOff == 1 && cOff == 1) continue;
						if (curr[r+rOff][c+cOff] == 0x7c) trees++;
						if (curr[r+rOff][c+cOff] == 0x23) lumberyards++;
					}
				}
				next[r+1][c+1] = curr[r+1][c+1];
				if (curr[r+1][c+1] == 0x2e && trees >= 3) {
					next[r+1][c+1] = 0x7c;
				}
				if (curr[r+1][c+1] == 0x7c && lumberyards >= 3) {
					next[r+1][c+1] = 0x23;
				}
				if (curr[r+1][c+1] == 0x23 && (lumberyards == 0 || trees == 0)) {
					next[r+1][c+1] = 0x2e;
				}
			}
		}

		trees = 0;
		lumberyards = 0;
		for (r = 0; r < 50; r++) {
			for (c = 0; c < 50; c++) {
				curr[r+1][c+1] = next[r+1][c+1];
				if (curr[r+1][c+1] == 0x7c) trees++;
				if (curr[r+1][c+1] == 0x23) lumberyards++;
			}
		}
	}
	printf("%ld\n", (long)trees * (long)lumberyards);
}

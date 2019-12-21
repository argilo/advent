/*
Copyright 2018 Clayton Smith

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

CREATE TABLE input (line TEXT);
.separator ~
.import 03-input.txt input

CREATE TABLE parsed_input (num INTEGER, offset_x INTEGER, offset_y INTEGER, width INTEGER, height INTEGER);
INSERT INTO parsed_input SELECT
  CAST(SUBSTR(line, 2, INSTR(line, " ")-2) AS INTEGER),
  CAST(SUBSTR(line, INSTR(line, " @ ") + 3, INSTR(line, ",") - INSTR(line, " @ ") - 3) AS INTEGER),
  CAST(SUBSTR(line, INSTR(line, ",") + 1, INSTR(line, ": ") - INSTR(line, ",") - 1) AS INTEGER),
  CAST(SUBSTR(line, INSTR(line, ": ") + 2, INSTR(line, "x") - INSTR(line, ": ") - 2) AS INTEGER),
  CAST(SUBSTR(line, INSTR(line, "x") + 1) AS INTEGER)
FROM input;

CREATE TABLE fabric (x INT, y INT, overlaps INT, num INT);
INSERT INTO fabric
WITH RECURSIVE range(coord) AS (SELECT 0 UNION ALL SELECT coord+1 FROM range LIMIT 1000)
SELECT x.coord, y.coord, COUNT(num), MIN(num) FROM range AS x, range AS y, parsed_input
WHERE x.coord >= offset_x AND y.coord >= offset_y AND x.coord < offset_x + width AND y.coord < offset_y + height
GROUP BY x.coord, y.coord;

SELECT COUNT(*) FROM fabric WHERE overlaps >= 2;

CREATE TABLE non_overlapping (num INT, area INT);
INSERT INTO non_overlapping SELECT num, COUNT(*) FROM fabric WHERE overlaps = 1 GROUP BY num;
SELECT parsed_input.num FROM non_overlapping, parsed_input WHERE non_overlapping.num = parsed_input.num AND area = width * height;

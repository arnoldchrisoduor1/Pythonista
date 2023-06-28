import math
import random

table_list = [[0] * 10 for i in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        table_list[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(table_list[i][j], end=", ")
    print()


import os
import math
directorio_actual= os.getcwd()
print(f"Current working directory: {directorio_actual}")

num = int(input("Enter an integer: "))
log = math.log2(num)
print(f"Log base 2 of {num} is: {log}")

floor_val = math.floor(log)
ceil_val = math.ceil(log)

print(f"Floor: {floor_val}")
print(f"Ceiling: {ceil_val}")
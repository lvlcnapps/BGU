from huffman import *
import time

start_time = time.time()
for i in range(100):
    freq_start("input2.txt")
end_time = time.time()
print("Time start: ", start_time)
print("Time end: ", end_time)
print("Time for freq_start: ", (end_time - start_time) / 100)

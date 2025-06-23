# import time

# data = "hello world"
# p = ""
# index = 0

# while index < len(data):
#     for c in range(ord('a'), ord('z') + 1):
#         trial = p + chr(c)
#         print(trial)
#         time.sleep(0.1)  # Wait for 1 second
#         if trial == data[:index + 1]:
#             p = trial
#             index += 1
#             break
#     if index < len(data) and data[index] == ' ':
#         p += ' '
#         print(p)
#         time.sleep(0.1)  # Wait for 1 second before continuing
#         index += 1





import time
import string

data = "Great work"
p = ""
index = 0

while index < len(data):
    for c in string.printable:  # Includes letters, digits, punctuation, space, etc.
        trial = p + c
        print(trial)
        time.sleep(0.1)  # Fast but visible delay
        if trial == data[:index + 1]:
            p = trial
            index += 1
            break

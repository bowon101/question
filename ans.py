sentences = [
    "Hello World",
    "Hello World Hello World",
    "Hello World Hello World Hello World",
]

sum = 0
for sentence in sentences:
    count_w = sentence.split(' ')
    # print(len(count_w))
    if count_w > sum :
        sum = len(count_w)
print(sum)
list_example = [1, 2, 3, 4, 5, 2]
count = 0
iterate = 0
while iterate < len(list_example):
    if list_example[iterate] == 2:
        count += 1
    iterate += 1
print(count, iterate)

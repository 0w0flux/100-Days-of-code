scores = [10, 23, 234, 24, 65, 86, 45, 234, 645, 344, 234, 564, 23]

max_score = scores[0]
for i in scores:
    if i > max_score:
        max_score = i

print(max_score)

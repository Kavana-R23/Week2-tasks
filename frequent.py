from collections import Counter


my_list = [1, 2, 2, 3, 1, 4, 2, 1, 1]

counter = Counter(my_list)
most_common_element, frequency = counter.most_common(1)[0]
print("Most frequent element:", most_common_element)
print("Frequency:", frequency)

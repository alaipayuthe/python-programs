def strange_sum(numbers):
    strangesum = 0
    for item in numbers:
        if item % 3 != 0:
            strangesum = strangesum + item

    return strangesum

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
            

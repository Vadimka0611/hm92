def difference (*numbers):
    if len(numbers) == 0:
        return 0
    res_min = min(*numbers)
    res_max = max(*numbers)
    res_str = res_max - res_min

    return round(res_str, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

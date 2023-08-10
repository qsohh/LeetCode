# Prime numbers for hashing 26 letters

```python
hash_num = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
```

# Transfer between char and digit

```python
char2digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
```

```python
digit2char = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
```


# Binary search reference

Search `target: int` in `numbers: List[int]`, which is non-decreasing.

Search `numbers[mp]` that is exactly EQUAL to `target` (so that `numbers` is strictly increasing):

```python
left, right, mid = 0, len(numbers) - 1, len(numbers)//2
while left < right:
    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
    mid = left + (right - left) // 2
return mid if numbers[mid] == target else False # consider the case if target not in the list
```

Search for `numbers[mp]` that is the MAXimum which is LESS than `target`:

```python
left, right, mid = 0, len(numbers) - 1, len(numbers)//2
while left < right:
    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        right = mid - 1
    else:
        left = mid
    mid = left + (right - left) // 2
return mid
```

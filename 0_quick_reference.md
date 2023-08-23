# Prime numbers for hashing 26 letters

```python
hash_letter2prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
```

```python
hash_prime2letter = {2: 'a', 3: 'b', 5: 'c', 7: 'd', 11: 'e', 13: 'f', 17: 'g', 19: 'h', 23: 'i', 29: 'j', 31: 'k', 37: 'l', 41: 'm', 43: 'n', 47: 'o', 53: 'p', 59: 'q', 61: 'r', 67: 's', 71: 't', 73: 'u', 79: 'v', 83: 'w', 89: 'x', 97: 'y', 101: 'z'}
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

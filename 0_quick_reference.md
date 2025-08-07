# Prime numbers for hashing 26 letters

```python
hash_letter2prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
```

```python
hash_prime2letter = {2: 'a', 3: 'b', 5: 'c', 7: 'd', 11: 'e', 13: 'f', 17: 'g', 19: 'h', 23: 'i', 29: 'j', 31: 'k', 37: 'l', 41: 'm', 43: 'n', 47: 'o', 53: 'p', 59: 'q', 61: 'r', 67: 's', 71: 't', 73: 'u', 79: 'v', 83: 'w', 89: 'x', 97: 'y', 101: 'z'}
```

# Prime numbers less than 1000
`tuple` version and `set` version
```python
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997)

PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997}
```

# Set of vowel letters

```python
VOWELS = {'a', 'e', 'i', 'o', 'u'}
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

or just 

```python
bisect.bisect_left(numbers, target, lo=left, hi=right, key==fct_key)
```

See also

```python
bisect.bisect_right(numbers, target, lo=left, hi=right, key=fct_key)
```

# Fermat's little thm related

As $a^{p-1} \equiv 1 \pmod{p}$ (attention to the hyps), it can be induced that $a^{p-2} \equiv a^{-1} \pmod{p}$.

```python
def InverseMod(a, m=MOD):
    return pow(a, m-2, m)

def PowerMod(a, p, m=MOD):
    return pow(a, p, m)

@cache
def FactorialMod(a, m=MOD):
    if a < 2:
        return 1
    return FactorialMod(a-1, m)*a%m
```

# Mo's algorithm

莫队算法

# Segment Tree

A segment tree is adapted for works like searching loacl sum/max or prefix sum/max.

To be refined as template.

The algorithmic structure of Segment Tree (local maximum, taking [LeetCode 3479](https://leetcode.com/problems/fruits-into-baskets-iii)):

```python
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SegmentTree(TreeNode):
    def __init__(self, data):
        if len(data) == 1:
            self.val = data[0]
            self.left = None
            self.right = None
        elif len(data) == 2:
            self.val = max(data)
            self.left = SegmentTree([data[0]])
            self.right = SegmentTree([data[1]])
        else:
            n = len(data)
            self.left = SegmentTree(data[:(n+1)//2])
            self.right = SegmentTree(data[(n+1)//2:])
            self.val = max(self.left.val, self.right.val)

    def pot(self):
        # Pre-order Traversal
        if not self.left:
            return str(self.val)
        return ", ".join([self.left.pot(), self.right.pot()])
    
    def search(self, target):
        # DFS search the target
        # if found, change the local max along all path if needed, return True; 
        # if not found, return False
        if self.val < target:
            return False
        if not self.left:
            self.val = 0
            return True
        if self.left.val >= target:
            self.left.search(target)
        else:
            self.right.search(target)
        self.val = max(self.left.val, self.right.val)
        return True
```

Flattened list structure:

```python
class SegmentTree():
    def __init__(self, data):
        n = len(data)
        self.size = 1
        while self.size <= n:
            self.size *= 2
        self.size = self.size*2
        self.tree = [0] * self.size
        self.tree[self.size//2:self.size//2+n] = data
        # For treenode at idx, its left child is at 2*idx, and right is at 2*idx+1
        for idx in range(self.size//2-1, -1, -1):
            self.tree[idx] = max(self.tree[2*idx], self.tree[2*idx+1])

    def search(self, target, idx=1):
        # DFS search the target
        # if found, change the local max along all path if needed, return True;
        # if not found, return False
        if self.tree[idx] < target:
            return False
        if idx >= self.size//2:
            self.tree[idx] = 0
            return True
        if self.tree[2*idx] >= target:
            self.search(target, 2*idx)
        else:
            self.search(target, 2*idx+1)
        self.tree[idx] = max(self.tree[2*idx], self.tree[2*idx+1])
        return True
```
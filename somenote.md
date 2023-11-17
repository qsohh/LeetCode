Found someone's submission for Pb 2910:

```Python
def get_cnt(count, x):
    # x, x + 1
    # (x+1)b + xa = count
    #
    a_plus_b, b = divmod(count, x)
    if a_plus_b < b:
        return -1
    return (count + x) // (x + 1)


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        freq = Counter(nums).values()
        
        for x in range(min(freq), 0, -1):
            result = 0
            for count in freq:
                cur_count = get_cnt(count, x)
                if cur_count == -1:
                    break
                result += cur_count
            else:
                return result
            
        
        return -1

def run():
    from inspect import signature
    from json import loads, dumps

    solution = Solution()

    func = None
    for attr_name in dir(solution):
        if attr_name.startswith('__'):
            continue
        attr_value = getattr(solution, attr_name)
        if callable(attr_value):
            if func is not None:
                raise Exception('There are multiple methods in Solution class')
            func = attr_value
    if func is None:
        raise Exception('The function in Solution class is not found')

    params_length = len(signature(func).parameters)

    input_file = open(0)
    output_file = open('user.out', 'w')

    try:
        while True:
            params = [loads(next(input_file)) for _ in range(params_length)]
            result = func(*params)
            output_file.write(dumps(result) + '\n')
    except StopIteration:
        exit()


run()
```

class Solution:
    def removedigit(self, num: str) -> str:
        for i, k in enumerate(num):
            if i == (len(num)-1):
                num = num[0:-1]
                return num
            if k > num[i+1]:
                num = num[0:i] + num[i+1:]
                return num.lstrip('0')
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= (len(num)-num.count('0')):
            return '0'
        for i in range(k):
            num = self.removedigit(num)
        return num.lstrip('0')

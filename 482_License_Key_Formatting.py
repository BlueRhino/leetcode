class Solution:
    @staticmethod
    def licenseKeyFormatting(S: 'str', K: 'int') -> 'str':
        s, k = S, K
        sr = s[::-1]
        i, total = 0, 0
        res = []
        for tmp in sr:
            if tmp == '-':
                continue
            else:
                i += 1
                total += 1
                res.append(tmp)
                if i == k:
                    i = 0
                    res.append('-')
        if res and res[-1] == '-':
            res = res[:-1]
        res = res[::-1]
        return ''.join(res).upper()


if __name__ == '__main__':
    print(Solution.licenseKeyFormatting('5F3Z-2e-9-w', 4))

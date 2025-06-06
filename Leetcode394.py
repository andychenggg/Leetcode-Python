class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        p = 0

        while p < len(s):
            if s[p].isdigit():
                _p = p
                while s[_p].isdigit():
                    _p += 1
                stack.append(int(s[p:_p]))
                p = _p
            elif s[p] == '[':
                stack.append('[')
                p += 1
            elif 'a' <= s[p] <= 'z':
                _p = p
                while _p < len(s) and 'a' <= s[_p] <= 'z':
                    _p += 1
                stack.append(s[p:_p])
                p = _p
            elif s[p] == ']':
                tmp = ""
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                tmp = stack.pop() * tmp
                stack.append(tmp)
                p += 1
        tmp = ""
        for s in stack:
            tmp += s
        return tmp



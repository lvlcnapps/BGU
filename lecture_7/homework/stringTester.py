class Tst:
    def __init__(self, s):
        self.s = s

    def is_balanced(self, s, index, stack):
        if index == len(s):
            return not stack

        char = s[index]
        matching_bracket = {')': '(', ']': '[', '}': '{', '>': '<'}
        open_brackets = set(matching_bracket.values())

        if char in open_brackets:
            stack.append(char)
        elif char in matching_bracket:
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return False

        return self.is_balanced(s, index + 1, stack)

    def __str__(self):
        return str(self.is_balanced(self.s, 0, []))



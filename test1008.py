"""编写一个函数，该函数接受一个括号字符串，并确定括号的顺序是否有效。如果字符串有效，则函数应返回true，如果字符串无效，则返回false。
示例
“()” => 真
“)(()))” => 假
“(” => 假
“(())((()())())” => 真
制约因素
0 <= 输入长度 <= 100
除了左括号 “(” 和右括号 “)” 之外，输入可以包含任何有效的ASCII字符。此外，输入字符串可能为空和/或根本不包含任何括号。不要将其他形式的括号视为括号（例如[ ]、{ }、< >）。"""
def valid_parentheses(s: str) -> bool:
    ss = 0
    for i in s:
        if i == '(':
            ss += 1
        elif i == ')':
            ss -= 1
        if ss < 0:
            return False
    if ss == 0:
        return True
    else:
        return False


assert valid_parentheses("  (") == False
assert valid_parentheses(")test") == False
assert valid_parentheses("") == True
assert valid_parentheses("hi())(") == False
assert valid_parentheses("hi(hi)()") == True

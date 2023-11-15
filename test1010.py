""" ISBN-10标识符的长度为十位数。前九个字符是数字0-9。最后一个数字可以是0-9或X，表示值为10。
如果数字之和乘以其位置模11等于零，则ISBN-10数字有效。
例如:
ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
它是一个合法的ISBN-10 :

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
例子
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false"""
def valid_ISBN10(isbn: str) -> bool:
    sum = 0
    if len(isbn) == 10:
        for i in range(9):
            if isbn[i] in '0123456789':
                sum += int(isbn[i]) * (i + 1)
            else:
                return False
        if isbn[-1] == 'X':
            sum += 10 * 10
        elif isbn[-1] in '0123456789':
            sum += int(isbn[-1]) * 10
        else:
            return False
    else:
        return False
    if sum % 11 == 0:
        return True
    else:
        return False


assert valid_ISBN10('1112223339') == True
assert valid_ISBN10('048665088X') == True
assert valid_ISBN10('1293000000') == True
assert valid_ISBN10('1234554321') == True
assert valid_ISBN10('1234512345') == False
assert valid_ISBN10('1293') == False
assert valid_ISBN10('X123456788') == False
assert valid_ISBN10('ABCDEFGHIJ') == False
assert valid_ISBN10('XXXXXXXXXX') == False
assert valid_ISBN10('123456789T') == False
assert valid_ISBN10('048665088XX') == False
assert valid_ISBN10('129300000T') == False
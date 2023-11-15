# 创建迭代器类型
class IT(object):
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration
        return self.counter

# 根据类实例化来创建一个迭代器
# obj1 = IT()
# v1 = next(obj1)
# print(v1)
# v2 = next(obj1)
# print(v2)
# v3 = next(obj1) # 抛出异常
# print(v3)

obj2=IT()
for i in obj2: # 首先会执行迭代器对象的__iter__方法回去返回值，一直去返回的执行next对象
    print(i)
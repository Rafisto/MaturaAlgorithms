class PostFixNotation:
    def __init__(self):
        self.stack = []
        self.top = -1

    def pop(self):
        if self.top == -1:
            return
        else:
            self.top -= 1
            return self.stack.pop()

    def push(self, i):
        self.top += 1
        self.stack.append(i)

    def centralFunction(self, ab):
        for i in ab:
            try:
                self.push(int(i))

            except ValueError:
                val1 = self.pop()
                val2 = self.pop()
                if i == '/':
                    self.push(val2 / val1)
                else:
                    switcher = {'+': val2 + val1, '-': val2 - val1, '*': val2 * val1, '^': val2 ** val1}
                    self.push(switcher.get(i))
        return int(self.pop())


if __name__ == '__main__':
    eval_string = '2 3 + 4 * 5 4 6 - * + 2 /'
    strconv = eval_string.split(' ')
    obj = PostFixNotation()
    print(obj.centralFunction(strconv))

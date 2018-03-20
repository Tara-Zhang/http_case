class a():
    global s
    s = 1
    @classmethod
    def e(cls):
        print(a)

class b():
    @classmethod
    def h(cls):
        print(s)

if __name__ == '__main__':
    b.h()

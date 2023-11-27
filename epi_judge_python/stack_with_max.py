from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self) -> None:
        self.maxx=[]
        self.l=[]

    def empty(self) -> bool:
        # TODO - you fill in here.
         return len(self.l)==0

    def max(self) -> int:
        # TODO - you fill in here.
        return self.maxx[-1]

    def pop(self) -> int:
        # TODO - you fill in here.
        val=self.l.pop()
        if val==self.maxx[-1]:
            self.maxx.pop()
        return val

    def push(self, x: int) -> None:
        # TODO - you fill in here.
        if not self.maxx :
            self.maxx.append(x)
        elif self.maxx and self.maxx[-1]<=x:
            self.maxx.append(x)
        self.l.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))

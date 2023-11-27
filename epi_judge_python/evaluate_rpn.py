from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    ops={
        '+':lambda x,y : x+y,
         '-':lambda x,y:x-y,
         '/':lambda x,y:int(x/y),
         '*':lambda x,y: x*y
    }
    res=[]
    for c in expression.split(','):
        if c in ops:
            s = res.pop()
            f=res.pop()
            res.append(ops[c](f,s))
        else:
            res.append(int(c))
    return res[-1]






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))

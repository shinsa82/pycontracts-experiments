from contracts import contract


@contract
def add(a: int, b: int):
    return a+b


@contract
def pos_add(a: 'int,>0', b: int):
    return a+b


add(1, 2)
pos_add(1, 2)

add(-1, 2)
# pos_add(-1, 2)


@contract(a=int, l='list[N]', returns='list[N+1]')
def prepend(a, l):
    l.insert(0, a)
    return l


l = prepend(3, [2, 1, 4])

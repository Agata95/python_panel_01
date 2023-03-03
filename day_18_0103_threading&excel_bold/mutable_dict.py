slowniczek = {"start": "Cos na start"}


def fn1():
    print(slowniczek)


def fn2upd():
    slowniczek['fn2upd'] = 'update'


fn1()
fn2upd()
fn1()

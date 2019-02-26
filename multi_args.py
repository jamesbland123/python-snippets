""" Multiple arg example """

def listTest(*l_of_args):
    print(l_of_args)

def dictTest(**d_of_args):
    print(d_of_args)


listTest("a", "b", "c", "d", "e")
dictTest(a="apple", b="baby", c="cat")
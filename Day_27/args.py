def add(*args):
    new_list = [n for n in args]
    print(sum(new_list))

add(1, 2, 3, 4, 5, 6, 7)

def calculate(n, **kwargs):

    n += kwargs["add"]
    print(n)

    n *= kwargs["multiply"]
    print(n)

calculate(13, add=5, multiply=20)
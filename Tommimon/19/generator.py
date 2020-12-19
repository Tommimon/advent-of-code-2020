def generator(n, string=''):
    if n == 0:
        print(string)
    else:
        generator(n - 1, string + 'a')
        generator(n - 1, string + 'b')


for i in range(16):
    generator(i)

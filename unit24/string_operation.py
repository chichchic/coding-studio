text = 'Hello, world'
replace_result = text.replace('world', 'Python')
table = str.maketrans('abcdefghijklmnopqrstuvwxyz',
                      'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(replace_result)
print(text.translate(table))
print(text)
print('python'.ljust(15).replace(' ', '*'), end=' ')
print('python'.center(15).replace(' ', '-'), end=' ')
print('python'.zfill(15))

format_specifier = 'I am %s %d' % ('python', 3)
world = 'world'
print(format_specifier)
use_format = 'Hello {world}. {format_specifier}. welcome to the beautiful {world}'.format(
    world=world, format_specifier=format_specifier)
print(use_format)
print(f'Hello, {format_specifier:<30} {world}')

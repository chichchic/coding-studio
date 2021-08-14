files = input().split()


print(list(map(lambda file: f'{int(file[0]):03d}.{file[1]}', [
      key.split('.') for key in files])))

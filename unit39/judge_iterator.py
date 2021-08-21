class TimeIterator:
    def __init__(self, start, end):
        self.init = start
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return self.__print_time(current)
        else:
            raise StopIteration

    def __getitem__(self, index):
        current = self.start + index
        if current < self.end:
            return self.__print_time(current)
        else:
            raise StopIteration

    def __print_time(self, time):
        hour = time // 3600 % 24
        min = time % 3600 // 60
        sec = time % 60
        return f'{hour:02d}:{min:02d}:{sec:02d}'


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    TimeIterator
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')

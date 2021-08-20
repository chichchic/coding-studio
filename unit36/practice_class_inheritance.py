class AdvancedList(list):
    def replace(self, target_value, replace_value):
        while target_value in self:
            target_index = self.index(target_value)
            self[target_index] = replace_value


x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}


# def calc_avg(dict):
#     result = 0
#     for value in dict.values():
#         result += value
#     return result / len(dict)


def calc_avg(dict):
    return sum(dict.values()) / len(dict)


print(calc_avg(maria))

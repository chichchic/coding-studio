class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, date = map(int, date_string.split('-'))
        if month >= 1 and month <= 12 and date >= 1 and date <= 31:
            return True
        else:
            return False


if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

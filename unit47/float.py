import math
import sys
from fractions import Fraction
x = 0.1 + 0.2
result1 = math.fabs(x - 0.3) <= sys.float_info.epsilon
print(result1)
result2 = math.isclose(0.1 + 0.2, 0.3)
print(result2)
print(Fraction('10/3'))  # 분수 표현

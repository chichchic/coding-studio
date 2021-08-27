# __init__.py가 들어있으면 해당 폴더를 패키지로 인식한다. (3.3버전 이상부터는 필요없으나 호환을 위해 작성하는것을 권장)
# .은 현재 패키지(폴더)를 의미

# from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
# from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

from .operation import *    # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
from .geometry import *     # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴

# 일부만 공개하고 싶을 경우
# __all__ = ['add', 'triangle_area']    # calcpkg 패키지에서 add, triangle_area 함수만 공개

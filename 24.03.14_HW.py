Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## 1번 ##
>>> print("100")
100
>>> print(100)
100
>>> print(50+50)
100
>>> print("50+50")
50+50
>>> # 정답: 4번 #
>>> 
>>> ## 2번 ##
>>> print("%d/%d = %d" %(5, 10, 5/10))
5/10 = 0
>>> # 정답: 3번 #
>>> 
>>> ## 3번##
>>> print("%04d"%876)
0876
>>> print("%5s"%"CookBook")
CookBook
>>> print("%1.1f"%123.45)
123.5
>>> 
>>> ## 4번 ##
>>> print("{2:d}{0:d}{1:d}".format(111, 222, 333))
333111222
>>> # 정답: 3번 #
>>> 
>>> ## 11번 ##
>>> print(int("1011", 2))
11
>>> print(int("1A", 16))
26
>>> 
>>> ## 13번 ##
>>> print(int("1002". 2))
SyntaxError: invalid syntax
>>> print(int("1008". 8))
SyntaxError: invalid syntax
>>> print(int("AAFG", 16))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(int("AAFG", 16))
ValueError: invalid literal for int() with base 16: 'AAFG'
>>> # 정답: 1, 2, 3번 #
>>> 
>>> ## 15번 ##
>>> num = 12345678

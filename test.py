Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def findbox(a, b, c):
   if a>b:
      biggest=a
   else:
      biggest=b

   if c>biggest:
      biggest=c

   return biggest

a=int(input("첫 번째 숫자 입력: "))
b=int(input("두 번째 숫자 입력: "))
c=int(input("세 번째 숫자 입력: "))

biggest=findbox(a, b, c)

print(a, b, c "중 가장 큰 수는 ", biggest, "입니다.")
SyntaxError: invalid syntax
>>> 
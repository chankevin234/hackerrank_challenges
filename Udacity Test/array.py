# array = [[5,4,2],[4,4,1],[8,9,0],3]
# print(array[0])

# x = 50
# def func():
#     global x
#     print('x is', x)
#     x = 2
#     print('changed', x)
# func()
# print('final is', x)

# s = 'hello world'
# print(s[3:5] + s[6])

# print('Test'.find('Test'))

# print("foo" > "ahmed")

# for i in [0,2,3]:
#     if i%2 == 0:
#         print('e')
#     elif i == 0:
#         print('0')
#     else: 
#         print('odd')

# True = False
# while True:
#     print(True)
#     break

# i=0
# while i<5:
#     if i%2 == 0:
#         i = i+2
#         continue
#     i = i-1
# print(i)

# x = ["a","b", "c"]
# y = ["d","e","f"]
# z = []
# i = 0
# while i<3:
#     z.append(x[i])
#     z.append(y[i])
#     i=i+1
# print(z)

x=[2,1,3,4]
y = []
for i in x[1:]:
    y.append(i*2)
print(y)
# def squar(x):
#     return x*x

# def multiply(func, arr_args):
#     result = []
#     for i in arr_args:
#         result.append(func(i))
#     return result

# total = multiply(squar,[1,2,3,4,5])

# print(total)
# def logger(msg):

#     def inner_logger():
#         print('log :', msg)

#     return inner_logger

# log_var = logger("log me ")
# log_var()

# num1 = int(input('enter number:'))
# powr = int(input('enter power:'))
# total = 0

# def powrd():
#     total = num1*num1
#     return powrd


# while(powr!=0):
#     call_again = powrd()
#     call_again()
#     --powr

# print(total)

def sumUp(numOne,numTwo):
     return numOne+numTwo

print(sumUp(3,5))
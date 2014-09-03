# def check(a, dic, d):
#     answer = ''
#     if str(a) in str(d):
#         return 'Fizz'
#     for x in dic:
#             answer = answer + dic[x][d%x*5:]
#     if not answer:
#         return d
#     return answer

# if __name__ == '__main__':
#     # a = int(raw_input('input u a: '))
#     # b = int(raw_input('input u b: '))
#     # c = int(raw_input('input u c: '))
#     a,b,c=3,5,7
#     dic = {a: 'Fizz', b: 'Buzz', c: 'Whizz'}
#     for x in xrange(1, 101):
#         print check(a, dic, x)

a=[str(i).find('3') > -1 and 'Fizz' or 'Fizz'[i % 3 * 4 : ] + 'Buzz'[i % 5 * 4 : ] + 'Whizz'[i % 7 * 5 : ] or i for i in range(1, 101)]
print a
b=['Fizz'[(str(3)not in str(i))*4:]or 'Fizz'[i % 3 * 4 : ] + 'Buzz'[i % 5 * 4 : ] + 'Whizz'[i % 7 * 5 : ] or i for i in range(1,101)]
print b
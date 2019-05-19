#! /usr/bin/python
#-*- coding:utf-8

#print('hello world')
#a=4
#print(4)
#a=input('请输入密码：')
#print(a)
#a,b,c=1,2,3
#print(b)
#a="halle world"
#a=1
#print(type(a))
#a,b,c,=1,2,3
#d=a & b
#print(d)

#a='a345a878a'
#b=a.replace('a','dd',2)
#print(b)


#a='123a245a789'
#b=a.split('a')
#print(b)
#c='-'.join(b)
#print(c)



#a='你好，我叫%s,今年%d岁'
#b=input('xinming')
#c=int(input('nianlin'))
#c=int(c)
#d=a %(b,c)
#print(d)

#a=' 123 '
#b=a.rstrip()
#print(b)


# a = (234, 456, 768, 345, 'a', 'd')
# print(sort(a))

#
# a='234234sdf342aefdafsdfa'
# b=a.split('a')
# c='-'.join(b)
# print(c)

# # a = 'Halle, 我叫%s，今年%d岁'
# b=input('请输入姓名:')
# c=int(input('年龄：'))
# d=a %(b,c)
#print(d)

# # import copy
# a=[123,23,234,[33,22],45,34,]
# b=a.copy()
# # b=copy.deepcopy(a)
# a[-3].append(55)
#
# print(a)
# #a.remove(23)
# #a.pop(3)
# # a.sort()
# # a.reverse()
# # b=['aa','s34']
# # # a.extend(b)
#
# # print(b)
# a={23,'ds',433,32}
# b=a.copy()
# a.remove(32)
# a.add(34)
# print(a)
# print(b)
#a={'name':['xiaomin','xiaohong'],'age':20}
# a=list(a)
#
# print(a)
# a={}
# # print(type(a))
# a=set()
# print(type(a))
# a=1
# # if a<7 :
# #     print("nihao")
# # else:
# #     print('hello world')
# a=input("请输入：")
# a=int(a)
# if 60 <= a <=79:
#     print("及格")
# elif a>=80 and a<=89:
#     print("优秀")
# elif a>=90 and a>=100:
#     print("非常优秀")
# else:
#     print("不及格")




# a=input("请输入：")
# if a.startswith('a') or a.startswith('A'):
#  if a.endswith('c'):
#    print(110)
#  elif a.startswith('a'):
#     print(120)
# elif a.endswith('c'):
#     print(130)
# else:
#     print(250)

# a=input("请输入：")
# if a.startswith('a') or a.startswith('A') and  a.endswith('c'):
#    print(110)
# elif a.startswith('a'):
#     print(120)
# elif a.endswith('c'):
#     print(130)
# else:
#     print(250)


# a=input('请输入:')
# a=int(a)
# if a%2==0:
#  if a%3==0:
#   print('hallo world')
#  elif a%2==0:
#   print('hello')
# elif a%3==0:
#     print('world')
# else:
#     print('123')
# a=1
# for b in range(1,101):
#  a=a+b
# print(a)
# print(sum(range(101)))
# a=0
# for i in range(1,10,2):
#     if i==8:
#         break
#     print(i)
# else:
#     print('hello')# for i in range(1,100):

#50
#a=0
# for i in range(100):
#     if i%2==0:
#        a-=i
#     else:
#         a+=i
# print(a)
# b = input('请输入一个数：')
# b =int(b)
# for i in range(3):
# import random
# a = random.randint(1,10)
# for c in range(3):
#  b = int(input('请输入一个数:'))
#  if a>b:
#     print('数大了')
#  elif a<b:
#     print('数小了')
#  elif a==b:
#     print('恭喜你猜对了')
#     break

# b=0
# b=int(b)

# for i in range(1,10):
#     # for j in range(1,i):
#  print(i)

#
# for i in range(1,10):
#     for j in range(1,i+1):
#         d = i * j
#         print('%d*%d=%-2d'%(i,j,d),end =' ' )
#     print()
# b,c=[],[]
# a=[11,99,33,66,55,44,77,22,88]
# for i in a:
#  if i <= 55:
#   b.append(i)
#   print(b)
#  elif i > 55:
#   c.append(i)



# elif a<b:
#     d=set()
#     print(c)








#
# # sum = 2
# for i in range(3,100):
#      for j in range(2,i):
#          if i%j == 0:
#              break
#      else:
#         sum += i
#  print(sum)
##############################################################################################
##############################################################################################
# 1111完数：
# for i in range(1,1000):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if a==i:
#      print(a)
# # 2222九九：
# for x in range(1,10):
#    for y in range(1,x+1):
#       print("{}*{}={}\t".format(x,y,x*y),end="    ")
#    print()
#
# # 3333任意范围内质数之和：
# def s(c,b):
#     a=0
#     for i in range(c,b):
#         for j in range(2,i):
#             if i % j== 0:
#                 break
#         else:
#          a += i
#     return a
# s(2,100)
# c=s(2,100)
# print(c)
# #
#
# # print(c)

#
# 44444水仙花数：
# for a in range(1,10):
#   for b in range(0,10):
#     for c in range(0,10):
#      x=a*100+b*10+c
#      y=a**3+b**3+c**3
#      if x == y:
#       print(y)
# # #
# 5555冒泡排序
# def s(b):
#     a = input('请输入一个数,以逗号分开:')
#     b = a.split(',')

#     for i in range(1,len(b)):
#         for j in range(0,len(b)-1):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1]=b[j+1],b[j]
#     return b
# s()
# #
# 6666选择法排序：
# a = input('请输入一个数,以逗号分开:')
# b = a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1):
#         if int(b[j]) > int(b[i]):
#             b[j],b[i]=b[i],b[j]
# print(b)
#
# # #77777 将字符串变成整数
# a=input('>>>>')
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b=b+j*10**i
# print(type(b))
# #
#
# 88888判断三角形：
# while True:
#     e=[1,2,3]
#     a=int(input('请输入第一条边'))
#     b=int(input('请输入第二条边'))
#     c=int(input('请输入第三条边'))
#     e[0],e[1],e[-1]=a,b,c
#     e.sort()
#     a,b,c=e[0],e[1],e[-1]
#     if a*a+b*b>c*c:
#        print('锐角')
#     elif a*a+b*b==c*c:
#         print('直角')
#     elif a*a+b*b<c*c:
#         print('钝角')
#     else:
#         print('不是三角形')
#
# 99999三个数随机组合：
# def s(a):
#     for i in a:
#         for j in a:
#             for k in a:
#                 if i != j and i != k and j != k:
#                     print( i,j,k)
# s(1)

    #
# 101010判断字符串是否回文
# def s(b):
# a= input('请输入一个字符串：')
# if not a:
#     print('请不要输入空字符串！')
#     b = input('请重新输入一个字符串：')
# c=reversed(list(a))
# if list(c) == list(a):
#     print('您所输入的字符串是回文')
# else:
#     print('您所输入的字符串不是回文')
# # s('2222')


# 111111111阶乘之和
# def x(n):
#     # n = int(input('>>>>'))
#     a = 1
#     b = 0
#     c = 1
#     while n >= c:
#         a = a * c
#         b = b + a
#         c = c + 1
#     print(b)
# x(2)


# #12121212 统计去除空行注释的行数：
# with open('a.txt','r',encoding='utf-8') as u:
#     a=u.readlines()
#     b=len(a)
#     for i in a:
#         if i.startswith('#') or i == '\n':
#             b-=1
# print(b)


# 1313131313打印列表中所有第一大和第二大的数
# a=[12,12,23,11,2,12,23]
# b=a.copy()
# b=list(set(b))
# b.sort()
# for i in a:
#     if i == b[-1] or i == b[-2]:
#         print(i)


# # 14141414统计去除空行注释的行数：
# with open('a.txt','r',encoding='utf-8') as u:
#     a=u.readlines()
#     b=len(a)
#     for i in a:
#         if i.startswith('#') or i == '\n':
#             b-=1
# print(b)


# 1515151515十进制转换十六进制
# a = int(input("输入数字："))
#
# # print("十进制数为：", a)
# # print("转换为二进制为：", bin(a))
# # print("转换为八进制为：", oct(a))
# print("转换为十六进制为：", hex(a))



#十转十六进制
# a=[str(x) for x in range(10)]+[chr(x) for x in range(97,103)]
# b=int(input('>>>.'))
# f=[]
# while True:
#     c=b%16
#     b=b//16
#     f.append(a[c])
#     if b==0:
#         break
# f.reverse()
# f=''.join(f)
# print('0x{}'.format(f))



# #把txt文件写入excel表格中
# import  xlwt
# with open('a.txt','r',encoding='utf-8') as f:
#  c=f.readlines()
# ff=xlwt.Workbook(encoding='utf-8')
# sheet=ff.add_sheet('文件')
# for i in range(len(c)):
#     k=c[i].split(',')
#     for j in range(len(k)):
#        sheet.write(i,j,k[j] )
# ff.save('b.xls')




#22.从键盘上输入若干个学生的成绩，统计出平均成绩并输出低于平均分的学生成绩，用输入负数结束输入
# while True:
#     c = []
#     a = input('请输入一个数,以逗号分开:')
#     if ',' in a:
#        b = a.split(',')
#        for i in b:
#            c.append(int(i))
#        d = sum(c)/len(c)
#        print('平均数{}'.format(d))
#        for j in c:
#            if d > j:
#               print('低于平均数{}'.format(j))
#     else:
#         break

###################################################################################################
###################################################################################################
#
# b=int(input('请输入：'))
# for i in range(20):
#     if b>20:
#         print()

# a=0
# b=1
# while b < 101:
#     a+=1
#     b-=1
#     print(a)






# a=[23,34,45,412]
# count = len(a)
# for i in range(1,count):
#     for j in range(0,count-1):
#         if  a[j] > a[j+1]:
#          a[i],a[j]=a[j],a[i]
#         print(len(a))





#
# c = []
# a = input('请输入一个数:')
# if ' ' in a:
#     b = a.split(' ')
#     for i in b:
#      c.append(int(i))
#      for x in range(1,len(c)):
#          for j in range(0,len(c)-1):
#             if a[j] > a[j+1]:
#                a[j], a[j+1]=a[j+1], a[j]
# # print(c)
#     #
# i = sum = 0
#
# while i <= 4:
#     sum += i
# #     i = i+1
#
# print(sum)



#
# #
# def s(b):
#     # a = input('请输入一个数,以逗号分开:')
#     # b = a.split(',')
#     for i in range(1,len(b)):
#         for j in range(0,len(b)-1):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1]=b[j+1],b[j]
#     print(b)
# s([12,4,5,6])
# print(type(s))
#
# a=4
# def d(a,b):
#     # global a
#     # a=5
#     print(a,b)
# d(213,33)
# # print(a)
#
# if __name__=='__main__':
# #  print('123')
# def s(b):
#     a=0
#     for i in range(1,b+1):
#      a+=i
#     return a
# # s(100)
# # # c=s(100)
# # print(s(100)+2)
#
# print(__name__)

# e=[
#    {'name':'美女','price':'399'},
#    {'name':'游艇','price':'99'},
#    {'name':'美女','price':'399'},
# ]
# print(e)
# c = []
# a = input('请输入购买的商品号:')
# if ' ' in a:
#  b = a.split(' ')
#  for i in b:
#   c.append(int(i))
#   print(type(c))

# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
# money=int(input("请输入您的总金额："))
# cart={}#定义一个空的购物车
# #商品列表
# for i in goods:
#     print(i["name"],i["price"])
#
# while True:
#     i2=input("请选择商品，y/Y结算；")
#     #如果选择结算，则退出循环
#     if i2.lower()=="y":
#         break;
#     for item in goods:
#         if item["name"]==i2:
#             name=item["name"]
#             #如果购物车已有该商品，数量+1，若美女，则新建字典用于存储商品信息
#             if name in cart.keys():
#                 cart[name]["num"]+=1;
#             else:
#                 cart[name]={"num":1,'sigle_price':item["price"]}
#     print(cart)
#     #结账
# all_prices=0
# for k,v in cart.items():
#     n=v['sigle_price']
#     m=v['num']
#     all_sum=n*m;
#     all_prices+=all_sum;
# if all_prices>money:
#     print("余额不足")
# else:
# #     print("消费：",all_prices)



#
# a= [
#     {"name": "猪年限定——白虎志", "price" :1999},
#     {"name": "猪年限定——青龙志", "price" :10},
#     {"name": "猪年限定——朱雀志", "price" :20},
#     {"name": "猪年限定——瑞麟志", "price" :998},
#     {"name": "猪年限定——玄武志", "price" :66},
# ]
# x={"good_list":[],"price_list":[]}
#
# #用户输入账户金额
# money=int(input("请输入您的账户金额："))
#
# #打印商品信息
# print(" 产品列表:")
# while True:
#     for k,v in enumerate(a,1):
#         for i in range(len(a)):
#             if  k-1==i:
#                 print(k,a[i]["name"],a[i]["price"])
#     #用户选择商品
#     q=int(input("请选择你喜欢的商品："))
#     print("你选择的商品是：",a[q-1]["name"],"花费：",a[q-1]["price"])
#     # #计算选择商品后的余额
#     assets=money-a[q-1]["price"]#
#     if assets>0:
#         x["good_list"].append(a[q-1]["name"])   #如果资金充足，将商品加入购物车，并结算
#         x["price_list"].append(a[q-1]["price"])
#         print("你目前的账户余额为：",assets,"¥")
    #     choose=input("继续购物，请按'c'；结账，请按'o'；显示信息，请按'l'；退出，请按'q'")
    #     #查看加入购物车的商品信息
    #     if choose=='l':
    #         for prod,val in enumerate(x["good_list"],1):
    #             print(prod,val)
    #             break
    #     elif choose=='q':
    #         print("谢谢惠顾")
    #         break
    #     elif choose=='c':
    #        continue
    #     elif choose=='o':
    #         total=sum(x["price_list"])
    #         if total>money:
    #             print("余额不足！ ！")
    #         else:
    #             print("谢谢，本次花费：",total,'¥',"余额：",money-total,"¥")
    #             break
    #     else:
    #         print("错误，请重新输入：")
    # else:
    #     print("对不起，您的账户余额不足！请充值！！！")
    #     break









# def _recharge(account_name):
#         database = _load_database()
#         print("您的账户当前余额为：%.2f " % _get_balance(account_name))
#     while True:
#         input_data = input("您正在进行充值...请输入充值金额(按b返回上一页,按q退出)：").
#            if re.match(pattern=r'^\d+.\d{1,2}$', string=input_data):
#     #输入的金额必须为数字,充值完毕写入库中,退出当前循环
#             if input_data.isdigit():#整数数字
#     else:#小数
#     amount = float(input_data)
# #     database[account_name]['balance'] += amount
#     _save_account(database)
#     ##获取到当前用户余额
#     curr_balance = _get_balance(account_name)
#     print('您已成功充值,您的余额为\033[32m%.2f\033[0m元' % curr_balance)
#     break
#     elif input_data == 'b':
#     break
#     elif input_data == 'q':
#     _logout(account_name)
#     else:
#     print("您输入的有误，请重新输入金额")
#


# a=[2,2,4,5,6]
# b=len(a)
# for i in range(b-1):
#     if i not in b:
#      a.append(i)
#      print(a)

# li=[1,2,3,4,5,1,2,3]
# new_li=[]
#   for i in li:1 li=[1,2,3,4,5,1,2,3]
# 2 new_li=[]
# 3 for i in li:
# 4     if i not in new_li:
# 5         new_li.append(i)
# 6 print(new_li)
#    if i not in new_li:
#          new_li.append(i)
# # print
#
# # 九九：
# def b():
#     for x in range(1,10):
#        for y in range(1,x+1):
#           print("{}*{}={}\t".format(x,y,x*y),end="    ")
#        print()
# b()


#
# 质数之和：
# a=0
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j== 0:
#             break
#     else:
#       a += i
# print(a)






#
# a=[]
# b=input('>>')
# c=a.split(',')
# if i in c:




# a = ['{}*{}={}'.format(i,j,i*j) for i in range(1,10) for j in range(1,1+i)]
# print(a)
# a=lambda x,y :print(x+y)
# a(1,3)

#
# s = open('b.txt','a',encoding='utf-8')
# for x in range(1,10):
#     for y in range(1,x+1):
#      s.write ("{}*{}={}\t".format(x,y,x*y))
#     s.write("\n")
# s.close()


# t= open('b.txt','r',encoding='utf-8')
# print(t.read())
# t.close()


# t= open('t.txt','wb')
# # t.write()
# # t.close()








# L=[1,2,4,5,7,8,]
# for i in range(0, len(L)):
#     b = []
#     for j in L:
#          b.append(j[i])
#     a1 = min(b)
#     a2 = max(b)
#     a3 = max(b.remove(max(b)))
#     print(a1)

# c=[]
# a=open('a.txt','r',encoding='utf-8')
# b=a.readlines()
# print(b)
# b.count('\n')
# print(len(b))
# # c.append(b)
# # c.count('\n')
# print(c)


# b.remove('#')
# print(len())


# a.close()
#if a.startswith('a') or a.startswith('A') and a.endswith('c'):

#
#
# with open('a.txt','',encoding='utf-8')as b:
#     b.write('12345')
#
# def qwe(b):
#     print('hello')
#     return 3453456
# qwe(5)
# a=qwe(5)
# print(qwe(5))
# # 111111阶乘之和


# a=(input('>>>'))
# if not a:
#     print('qin')
#     a=(print('>>>>'))
# b=reversed(list(a))
# if list(a)==list(b):
#     print('hu')
# else:
#     print('bs')



# try:
#     a=100
#     print(a)
# except  :# 默认预防所有错误
#     print('fdgsd')
# else:
#     print(3452345)
# finally:
#     print(3244523)


# a=[23,34,12,4]
# print(sum(a))
# print(max(a))
# print(min(a))






# class siri():
#     def 嗨(self):
#         a=6
#         if a>3:
#          print('你好')
#         else:
#             print('haha')
#             self.__天气()
#     def __天气(self):
#         print('天气')
#
# # q=siri()
# # q.嗨()
# # class 小娜(siri):
# #     pass
# #     # def 嗨(self):
# #     #     print('阿萨德')
# # w=小娜()
# # w.嗨()
# e=siri()
# e.嗨()
#
# class h():
#     def __init__(self,a):
#         self.name=a
#     def 打电话(self):
#         print('打电话给{}'.format(self.name))
#     def 手动(self):
#             print('打手动给{}'.format('hah'))
# s=h('哈达')
# s.打电话()
# s.手动()
# #
# import  xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('文件')
# for i in range (1,10):
#     for j in range(1,i+1):
#          a=sheet.write(i-1,j-1,"{}*{}={}".format(i,j,i*j))
# f.save('a.xls')


# for x in range(1,10):
#    for y in range(1,x+1):
#       print("{}*{}={}\t".format(x,y,x*y),end="    ")
#    print()



# #把txt文件写入excel表格中
# import  xlwt
# with open('a.txt','r',encoding='utf-8') as f:
#  c=f.readlines()
# ff=xlwt.Workbook(encoding='utf-8')
# sheet=ff.add_sheet('文件')
# for i in range(len(c)):
#     k=c[i].split(',')
#     for j in range(len(k)):
#        sheet.write(i,j,k[j] )
# ff.save('b.xls')


#
# import xlrd
# f=xlrd.open_workbook('b.xls')
# sheet=f.sheets()[0]
# b=sheet.nrows
# with open('b.txt', 'w',encoding='utf-8') as t:
#  for i in range(b):
#    t.write(str(sheet.row_values(i))+'\n')

# for i in range(b):
#  t.write(str(st.row_values(i))+'\n')


# b = open('a.txt','r',encoding='utf-8')
# # print(b.read())
# # b.close()
#
#
# import xlrd
# f=xlrd.open_workbook('a.xls')
# b=f.nsheets
# print(b)
# b=f.sheet_names()
# print(b)
# sheet = f.sheet_by_name('内容')
# sheet = f.sheets()[0]
# b= sheet.col_values(2)
# print(b)
# c=sheet.nrows
# for i in range(c):
#     b = sheet.row_values(i)
#     print(b)
# c=sheet.ncols
# print(c)
# b=sheet.cell(1,0).value
# c=sheet.cell(1,1).value
# print(b,c)

# def s(a=0,b=200):
#     for i in range(2,b):
#         for j in range(2,i):
#            if
#                 break

# import xlwt
# with open('a.txt','r',encoding='utf-8') as f:
#     b=f.readlines()
# j=xlwt.Workbook(encoding='utf-8')
# sheet=j.add_sheet('hh')
# for i in range(len(b)):
#     k=b[i].split(',')
#     for z in range(len(k)):
#      sheet.write(i,z,k[z])
# j.save('a.xls')




# from xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('a.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(5-1,5-1,'是的范德萨')
# new_f.save('b.xls')
#
# import time
# # a=time.time()
# # print(a)
# # a=time.localtime ()
# a=input('>>>')
# b=time.strptime(a,'%Y-%m-%d')
# print(b)


# d=(2019,3,26,0,0,0,0,0,0)
# a=(1998,2,11,0,0,0,0,0,0)
# b=time.mktime(d)
# print(b)

# for i in range(10):
#     print(i)
#     time.sleep(1)
# import time
# a=input('>>>')


# # 爬虫文字
# import requests
# import re
# import xlwt
# for k in range(0,6):
#  a = 'https://www.qiushibaike.com/text/page/{}/'.format(k)
#  oo={
#     'User - Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 65.0) Gecko/20100101Firefox/65.0'
#  }    #发送请求
#  b=requests.get(a,headers=oo)
#                                                      #接受响应
#                                                     #  1.text 文本读取方式(字符串)
#                                                      #  2.content 以字节的方式接收
#
#
#
#
#  c=b.content.decode('utf-8')
#  zz=re.compile('<h2>(.*?)</h2>',re.S)
#  aa=zz.findall(c)
#  ff = []  # print(b.content.decode('utf-8'))#(网页源代码
#  qq = []
#  d=re.compile('<div class="content">(.*?)</span>',re.S)
#  f=d.findall(c)
#  for j in aa:
#      j=j.replace('\n','')
#      qq.append(j)
#  for i in  f:
#     i=i.replace('<span>','')
#     i=i.strip()
#     i=i.replace('<br/>','')
#     ff.append(i)
#  for x in range(len(ff)) :
#      ff.insert(x*2,qq[x])
#  with open('b.txt','a',encoding='utf-8') as g:
#     for i in ff:
#         g.write(i+'\n')
# with open('b.txt','r',encoding='utf-8') as f:
#  c=f.readlines()
# ff=xlwt.Workbook(encoding='utf-8')
# sheet=ff.add_sheet('文件')
# for i in range(len(c)):
#     k=c[i].split('\n')
#     for j in range(len(k)):
#        sheet.write(i,j,k[j] )
# ff.save('b.xls')



# import requests
# import re
# import xlwt
# a='https://www.zhipin.com/c101210100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page=1&ka=page-{}'.format(2)
# oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
# }
# ss=[]
# mm=[]
# b=requests.get(a,headers=oo)
# c=b.content.decode('utf-8')
# zz=re.compile('<div class="job-title">(.*?)</div>')
# m=re.compile('<span class="red">(.*?)</span>')
# w=re.compile('<p>(.*?)<em class="vline">')
# m1=m.findall(c)
# print(m1)
# for j in  m1:
#     ss.append(j)
# q=zz.findall(c)
# for i in  q:
#     mm.append(i)
# for x in range(len(ss)) :
#      ss.insert(x*2,mm[x])
#      print(ss)
# with open('b.txt','w',encoding='utf-8') as g:
#     for i in ss:
#         g.write(i+'\n')

#
# 爬虫图片：
# import requests
# import re
# class tp(object):
#     def 发送请求(self,qw):
#         url='https://www.qiushibaike.com/imgrank/page/{}/'.format(qw)
#         head={'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:65.0)Gecko/20100101Firefox/65.0'
#         }
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def 过滤(self,abc):
#         lianjie=[]
#         patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             new_a=re.compile(r'<img src="(.*?)"',re.S)
#             aaa=new_a.findall(i)
#             lianjie.extend(aaa)
#         return lianjie
#     def save(self,shu):
#         for a,i in enumerate(shu):
#             res =requests.get('https:'+i)
#             js=res.content
#             with open('yy\{}.jpg'.format(a),'ab') as f:
#                 f.write(js)
# tu=tp()
# for i in range(1,3):
#     ss=tu.发送请求(i)
#     ah=tu.过滤(ss)
#     tu.save(ah)

#
# import requests
# import re
# import xlrd
# class tp(object):
#     def 发送请求(self,qwer):
#         url = 'https://movie.douban.com/top250?start={}&filter='.format(qwer)
#         head={
#              'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:65.0)Gecko/20100101Firefox/65.0'
#              }
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return  html
#     def 过滤(self, abc):
#         lianjie=[]
#         patt=re.compile(r'<div class="pic">(.*?)</a>',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             new_a=re.compile(r'src="(.*?)"',re.S)
#             aaa=new_a.findall(i)
#             lianjie.extend(aaa)
#         print(lianjie)
#         return lianjie
#     def save(self,shu):
#         for a,i in enumerate(shu):
#             res =requests.get('https:'+i)
#             js=res.content
#             with open('{}.jpg'.format(a),'wb') as f:
#                 f.write(js)
# tu=tp()
# ss=tu.发送请求(25)
# ah=tu.过滤(ss)
# print(ah)
# tu.save(ah)
# print(tu)

# import requests
# import re
# import xlrd
# import xlwt
# from xlutils.copy import copy
# class tp(object):
#     def fsqq(self,qwer):
#         url = 'https://movie.douban.com/top250?start={}&filter='.format(qwer)
#         head={
#              'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:65.0)Gecko/20100101Firefox/65.0'
#              }
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return  html
#     def gl(self,abc):
#         ddd=[]
#         a=re.compile(r'alt="(.*?)" ',re.S)
#         aa = a.findall(abc)
#         # print(aa)
#         b=re.compile(r'导演: (.*?) ',re.S)
#         bb= b.findall(abc)
#         # print(bb)
#         c= re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
#         cc = c.findall(abc)
#         # print(cc)
#         d= re.compile(r'<span property="v:best" content="10.0"></span>(.*?)</div>', re.S)
#         dd = d.findall(abc)
#         for m in dd:
#          new_a=re.compile(r'<span>(.*?)</span>',re.S)
#          ui=new_a.findall(m)
#          ddd.extend(ui)
#         # print(ddd)
#         return aa,bb,cc,ddd
#
#     def save(self,qq,ww,ee,rr):
#       try:
#           ff=xlrd.open_workbook('ss.xls')
#           sheet1 = ff.sheets()[0]
#           num=sheet1.nrows
#           new_f=copy(ff)
#           sheet=new_f.get_sheet(0)
#           for i,j in enumerate(ww):
#               sheet.write(num+i,0,j)
#               sheet.write(num+i,1,rr[i])
#               sheet.write(num+i,2,ee[i])
#               sheet.write(num+i,3,qq[i])
#           new_f.save('ss.xls')
#       except:
#             ff = xlwt.Workbook()
#             sheet=ff.add_sheet('豆瓣')
#             sheet.write(0,0,'片名')
#             sheet.write(0, 1, '导演')
#             sheet.write(0, 2, '评分')
#             sheet.write(0, 3, '评价')
#             for o,p in enumerate(ww):
#                 sheet.write(o+1,0,p)
#                 sheet.write(o+1,1,rr[o])
#                 sheet.write(o+1,2,ee[o])
#                 sheet.write(o+1,3,qq[o])
#             ff.save('ss.xls')
# tu = tp()
# for l in range(0,100,25):
#  ss = tu.fsqq(l)
#  qq,ww,ee,rr=tu.gl(ss)
#  tu.save(qq,ww,ee,rr)



    # def save(self,shu):
    #     for a,i in enumerate(shu):
    #         res =requests.get('https:'+i)
    #         js=res.content
    #         with open('{}.jpg'.format(a),'wb') as f:
    #             f.write(js)
# tu=tp()
# ss=tu.发送请求(25)
# ah=tu.过滤(ss)
# print(ah)
# # tu.save(ah)

# import re
# import requests
# import xlrd
# import xlwt
# from xlutils.copy import copy
#
# class douban_name(object):
#     def wangzhi(self,sl):
#         wz='https://movie.douban.com/top250?start={}&filter='.format(sl)
#         leixing={
#             'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 66.0)Gecko/20100101Firefox/66.0'
#         }
#         res = requests.get(wz, headers=leixing)
#         html=res.content.decode('utf-8')
#         # print(html)
#         return html
#     def filter(self,ft):
#         director=re.compile('导演:(.*?)&nbsp',re.S)
#         daoyan=director.findall(ft)
#         name=[]
#         movie_name=re.compile(' <div class="pic">(.*?)</a>',re.S)
#         movie_name_1=movie_name.findall(ft)
#         for dy_name in movie_name_1:
#             movie=re.compile(r'<img width="100" alt="(.*?)"',re.S)
#             names=movie.findall(dy_name)
#             name.append(names)
#             # print(names)
#         pingfen=[]
#         pingjia=[]
#         pingfen_2=re.compile('<div class="star">(.*?)</div>',re.S)
#         pingfen_1=pingfen_2.findall(ft)
#         # print(pingfen_1)
#         for pj in pingfen_1:
#             score_1=re.compile('<span class="rating_num" property="v:average">(.*?)</span>',re.S)
#             evaluate = re.compile('<span>(.*?)评价</span>', re.S)
#             pingfen.append(score_1.findall(pj))
#             pingjia.append(evaluate.findall(pj))
#         # print(daoyan)
#         # print(name)
#         # print(pingfen)
#         # print(pingjia)
#         return daoyan,name,pingfen,pingjia
#     def baocun(self,d,n,f,j):
#         try:
#             q=xlrd.open_workbook('bb.xls')
#             sheet=q.sheets()[0]
#             hang=sheet.nrows
#             new_q=copy(q)
#             sheet_1=new_q.get_sheet(0)
#             for k ,kk in enumerate(d):
#                 sheet_1.write(hang+k,0,kk)
#                 sheet_1.write(hang+k,1,n[k])
#                 sheet_1.write(hang+k,2,f[k])
#                 sheet_1.write(hang+k,3,j[k])
#             new_q.save('bb.xls')
#         except:
#             q=xlwt.Workbook()
#             sheet=q.add_sheet('豆瓣电影')
#             sheet.write(0,0,'导演')
#             sheet.write(0,1,'电影名')
#             sheet.write(0,2,'评分')
#             sheet.write(0,3,'评价')
#             for y,xx in enumerate(n):
#                 sheet.write(y+1,0,d[y])
#                 sheet.write(y+1,1,xx)
#                 sheet.write(y+1,2,f[y])
#                 sheet.write(y+1,3,j[y])
#             q.save('bb.xls')
# db=douban_name()
# for aa in range(0,100,25):
#     yshu=db.wangzhi(aa)
#     d,n,f,j=db.filter(yshu)
#     db.baocun(d,n,f,j)
#

# import requests
# import json
# url ='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.244287|34.73613|114.548471|34.863558&keywords=洗浴中心'
# res=requests.get(url)
# qwe=res.text
# asd=json.loads(qwe)
# qq=(asd['data']['poi_list'][0]['name'])
# print(qq)


# import pymysql
# conn=pymysql.connect(
#     host="192.168.1.12",  # 数据库主机地址
#     port=3306,
#     user="root",  # 数据库用户名
#     passwd="123456") # 数据库密码

#(创建游标   类似于vim光标
# aa=conn.cursor()#)
#执行sql语句
# aa.execute('create database py;')
# aa.execute('use py;')
# aa.execute('create table pyb(name char(255), age int,xb char(255), cj int);')
# aa.execute('select * from pyb;')
# aa.execute('show tables;')
# for i in range(100):
  # aa.execute('insert into pyb values("{}",{},"{}",{});'.format(123,12,12,123))
 #  conn.commit()
# aa.execute('select * from pyb;')
# a=aa.fetchmany(3)
 # a=aa.fetchall()
#a=aa.fetchone()


# aa.execute('use py_test;')
# #fetchall () 获取上一个sql语句的结果   想要获取多个就在每个sql语句后面加 fatchall
#fetchmany() 获取上一个sql语句的结果  默认只获取结果中的第一个数据 括号里面传入数字写几就获取几个
#fetchone() 每次只获取一条结果
# conn.close() 断开连接
#conn.commit() 提交 (更新，删除，添加)
# a=aa.fetchall()
# print(a)

#
# import pymysql
# conn=pymysql.connect(
#     host="192.168.1.12",
#     port=3306,
#     user="root",
#     passwd="123456")
# while True:
#     aa=conn.cursor()
#     ss=aa.execute(input('查看数据库：'))
#     a = aa.fetchall()
#     print(a)
#     cc=aa.execute( input('切换数据库：'))
#     f = aa.fetchall()
#     print(f)
#
# import re
#
# import xlrd
# import xlwt
# import requests
# import json
# from xlutils.copy import copy
# class tp(object):
#     def fsqq(self,wer):
#             url ='https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&=0&_v=0.55091875&x-zp-page-request-id=f29f54677e114cafa84557f276bed884-1554121531373-919481'.format(wer)
#             leixing={'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:66.0)Gecko/20100101Firefox/66.0'
#             }
#             res=requests.get(url,headers=leixing)
#             html=res.content.decode('utf-8')
#             return html
#             # qwe=res.text
#             # asd=json.loads(qwe)
#             # return asd
#     def op(self,uio):
#         zz, xx, cc, vv, bb, nn = [], [], [], [], [], []
#         asd = json.loads(uio)
#         aa=len(asd['data']['results'])
#         for k in range(aa):
#             qian = (asd['data']['results'][k]['salary'])
#             zz.append(qian)
#             zhiwei = (asd['data']['results'][k]['jobName'])
#             xx.append(zhiwei)
#             xueli = (asd['data']['results'][k]['eduLevel']['name'])
#             cc.append(xueli)
#             diqu = (asd['data']['results'][k]['city']['display'])
#             vv.append(diqu)
#             gongshi = (asd['data']['results'][k]['company']['name'])
#             bb.append(gongshi)
#             baozhang = (asd['data']['results'][k]['jobTag']['searchTag'])
#             nn.append(baozhang)
#         return zz,xx,cc,vv,bb,nn
#     def save(self,qq,ww,ee,rr,tt,yy):
#        try:
#           ff=xlrd.open_workbook('zl.xls')
#           sheet1 = ff.sheets()[0]
#           num=sheet1.nrows
#           new_f=copy(ff)
#           sheet=new_f.get_sheet(0)
#           for k,j in enumerate(qq):
#               sheet.write(num+k,0,j)
#               sheet.write(num+k,1,ww[k])
#               sheet.write(num+k,2,ee[k])
#               sheet.write(num+k,3,rr[k])
#               sheet.write(num+k,4,tt[k])
#               sheet.write(num+k,5,yy[k])
#               new_f.save('zl.xls')
#        except:
#             ff = xlwt.Workbook()
#             sheet=ff.add_sheet('智联招聘')
#             sheet.write(0,0,'薪资')
#             sheet.write(0,1, '职位')
#             sheet.write(0,2, '学历')
#             sheet.write(0,3, '市(区)')
#             sheet.write(0,4, '公司')
#             sheet.write(0,5, '福利')
#             for o,p in enumerate(qq):
#                 sheet.write(o+1,0,p)
#                 sheet.write(o+1,1,ww)
#                 sheet.write(o+1,2,ee)
#                 sheet.write(o+1,3,rr)
#                 sheet.write(o+1,4,tt)
#                 sheet.write(o+1,5,yy)
#                 ff.save('zl.xls')
# tu = tp()
# for l in range(0,180,90):
#     zxc=tu. fsqq(l)
#     qq,ww,ee,rr,tt,yy=tu.op(zxc)
#     tu.save(qq,ww,ee,rr,tt,yy)

#
# import pymysql
# conn=pymysql.connect(
#     host="192.168.1.6",  # 数据库主机地址
#     port=3306,
#     user="root",  # 数据库用户名
#     passwd="123456") # 数据库密码
# aa=conn.cursor()#)
# aa.execute('create database oo;')
# aa.execute('use oo;')
# aa.execute('create table te')
# a = aa.fetchall()

number_l = [100,97,4,89,34,2]
# for i in range(0,len(number_l)):
    # number_l.append(input("number:"))
#     print(i)

print(len(number_l))
# for i in range(0,len(number_l)-1):
#     print(i)

for i in range(0,len(number_l)-1):
    print("第"+str(i+1)+"趟")
    for n in range(0,len(number_l)-i-1):
        print("第"+str(n+1)+"次")
        if number_l[n] > number_l[n+1]:     #0>1,1>2,2>3,3>4,4>5
            number_l[n],number_l[n+1] = number_l[n+1],number_l[n]
        # print(number_l)

'''
6
第一次
0
0-5
0>1,1>2,2>3,3>4,4>5
第二次
1
0-4
0>1,1>2,2>3,3>4
第三次
2
0-3
0>1,1>2,2>3
第四次
3
0-2
0>1,1>2
第五次
4
0-1
0>1
第五次
5
0-0
0>1

'''
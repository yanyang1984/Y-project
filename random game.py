import random
number=random.randint(0,100)
i=1
print('数字游戏0~100')
while True:
    #print(number)
    num=input('输入数字：')
    num=float(num)
    if i == 5:
        print('您的机会用完了')
        con = input('按任意键继续,输入0退出')
        if con =='0':
            break
        else:
            number = random.randint(0,100)
            i=1
    elif num<0 or num>100:
        print('输入0~100的数字:')
    elif num < number:
        time=5-i
        i=i+1
        print('猜小了，请重新猜测，您还有%s机会:'%time)
    elif num > number:
        time=5-i
        i=i+1
        print('猜大了，请重新猜测，您还有%s机会：'%time)
    else:
        print('您猜对了')
        con=input('按任意键继续游戏,输入0退出:')
        if con=='0':
            break
        else:
            number=random.randint(0,100)
            i=1  

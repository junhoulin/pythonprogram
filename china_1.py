SQL101 = None  # 定义 SQL1 变量并初始化为 None
SQL202 = None  # 定义 SQL2 变量并初始化为 None

def languagechina():
    global SQL101, SQL202
    lock = 'NO'  # 初始化 lock 变量
    while lock == 'NO':
        SQL101 = input("请输入SQL1语法： ")
        SQL202 = input("请输入SQL2语法： ")

        print(SQL101+"( Number )"+SQL202)
        lock = input("是否锁定SQL1、SQL2？(输入YES或NO)：")
        
        if lock == "YES":
            print("語法已鎖定")
            break  # 结束循环     

def EnterData(SQL101,SQL202):
    quanlity = int(input('資料數量多少'))
    my_list = []
    for i in range(quanlity): 
        value = input("請輸入%s個值："% i)
        my_list.append(value)    
        # 打印列表中的所有值
    print("合併後的SQL語法：")
    for item in my_list:
        print(str(SQL101)+item+str(SQL202))
languagechina()
EnterData(SQL101,SQL202)


input("退出程序")
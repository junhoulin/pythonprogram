SQL101 = None  
SQL202 = None  
GOGO = 'gogo'
my_list = []

## 輸入資料和數量的FUNCTION  
def EnterData(my_list):
    quanlity = int(input('資料數量多少: '))
    for i in range(quanlity): 
        value = input("請輸入%s個值： "% i)
        while value in my_list:
            print("已經重複輸入了 = = ")
            value = input("請輸入%s個值： " % i)

        my_list.append(value)    
        
## 輸入語法並加入資料
def languagechina(my_list):
    global SQL101, SQL202
    lock = 'NO'  
    while lock == 'NO':
        SQL101 = input("请输入SQL1语法： ")
        SQL202 = input("请输入SQL2语法： ")

        print(SQL101+"( Number )"+SQL202)
        lock = input("是否锁定SQL1、SQL2？(输入YES或NO)： ")
        
        if lock == "YES":
            print("語法已鎖定")
            break   
    print("合併後的SQL語法： ")
    for item in my_list:
        print(str(SQL101)+item+str(SQL202))

## 調用上面兩個FUNCTION
EnterData(my_list)
while GOGO == 'gogo':
    languagechina(my_list)
    GOGO = input("gogo OR stop : ")
    if GOGO == "STOP":
        break
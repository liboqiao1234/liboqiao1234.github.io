import json
import os
def add():
    num=int(input("请输入清单号码:"))
    name=input("请输入待办事项:")
    time=input("请输入截止日期:")
    importance=input("请输入重要程度:")
    old=json.load(open("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/data.json","r",encoding="UTF-8"))
    data=[name,time,importance]
    old["list"][num-1][2].append(data)
    old["list"][num-1][1]=old["list"][num-1][1]+1
    json_str=json.dumps(old,ensure_ascii=False) 
    with open("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/data.json","w",encoding="utf-8") as file_obj:
        file_obj.write(json_str)
    file_obj.close();
def finish():
    old=json.load(open("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/data.json","r",encoding="UTF-8"))
    for i in range(0,old["user"][1]):
        print("清单",i+1,old["list"][i][0])
        for j in range(0,old["list"][i][1]):
            print(j+1,end=":")
            print(old["list"][i][2][j][0],old["list"][i][2][j][1])
        print()
    nn=0
    while nn!=-1:
        nn=int(input("请输入完成的清单编号\n"))
        mm=int(input("请输入序号\n"))
        del old["list"][nn-1][2][mm-1]
        old["list"][nn-1][1]=old["list"][nn-1][1]-1
        for i in range(0,old["user"][1]):
            print("清单",i+1,old["list"][i][0])
            for j in range(0,old["list"][i][1]):
                print(j+1,end=":")
                print(old["list"][i][2][j][0],old["list"][i][2][j][1])
            print()
    json_str=json.dumps(old,ensure_ascii=False) 
    with open("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/data.json","w",encoding="utf-8") as file_obj:
        file_obj.write(json_str)
    file_obj.close();


op=int(input("请输入选项:0完成，1增加\n"))
if(op==1):
    add()
elif(op==0):
    finish()
os.system("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/update.bat")

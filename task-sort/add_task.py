import json
import os
num=int(input("请输入清单号码:"))
name=input("请输入待办事项:")
time=input("请输入截止日期:")
importance=input("请输入重要程度:")
old=json.load(open("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/data.json","r",encoding="UTF-8"))
data=[name,time,importance]
old["list"][num-1].append(data)
json_str=json.dumps(old,ensure_ascii=False)
with open("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/data.json","w",encoding="utf-8") as file_obj:
    file_obj.write(json_str)
file_obj.close();
os.system("E:/workspace/mygithubio/liboqiao1234.github.io/task-sort/update.bat")

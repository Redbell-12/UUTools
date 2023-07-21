#-*-coding:utf-8-*-
import os
import socket
import winreg
  
#检测主机名，并将主机名作为检测结果的文件名
#Detect your hostname and use it to name the result file.
hostname = socket.gethostname()

#保存在D盘目录，使用新建模式
#add a new file in disk D.
#file = open(r'D:\%s.txt' % hostname, 'w', encoding='utf8')
#保存在当前目录，使用新建模式
#add a new file in the current floder.
file = open(r'%s.txt' % hostname, 'w', encoding='utf8')
  
#定义检测位置
#to define the position
sub_key = [
    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', 
    r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall'
]

#读取注册表，循环获取所有的软件列表信息
#read the regdit list, get all the software's name
software_name = []
for i in sub_key:
    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, 
        i, 
        0, 
        winreg.KEY_ALL_ACCESS
    )
    for j in range(0, winreg.QueryInfoKey(key)[0]-1):
        try:
            key_name = winreg.EnumKey(key, j)
            key_path = i + '\\' + key_name
            each_key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE, 
                key_path, 
                0, 
                winreg.KEY_ALL_ACCESS
            )
            DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
            DisplayName = DisplayName.encode('utf-8')
            software_name.append(DisplayName)
        except WindowsError:
            pass

software_name = list(set(software_name))
software_name = sorted(software_name)
try: 
    for result in software_name:
        app_name=str(result, encoding='utf-8')
        file.write(app_name + '\n')
        print(app_name)
except Exception as e:
    print(e)
finally:
    file.close()
	

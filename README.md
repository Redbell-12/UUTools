# UUTools
Uncommonly used tools. BUT useful


1.GetAllSoftNames.py
重装电脑前需要对现有软件进行整理和导出，运行后可以获取当前windows电脑中的软件列表，便于重装系统后按图索骥。  
Robot translate:Before reinstalling the computer, it is necessary to organize and export the existing software. After running, you can obtain a list of software in the current Windows computer, which is convenient to follow the diagram after reinstalling the system.   
目前导出到当前目录，运行在python3，在win10和win11环境下均可正常使用  
RUN:python3 GetAllSoftNames.py  
RESULT:DESKTOP-xxxxxx.txt  

排错：  
1.1PermissionError: [WinError 5] 拒绝访问。  
使用“管理员运行即可”，读取注册表权限问题  


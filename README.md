# Raspberry-Pi
Raspberry Pi Script Tools

开机启动

方法1：
只需要向 /etc/rc.local 文件中添加一句话，即可开机执行一个脚本

方法2：
在 /home/pi/.config 下创建一个文件夹，名称为 autostart，并在该文件夹下创建一个xxx.desktop文件（文件名以.desktop结尾，前面可以自定义），文件内容如下：

[Desktop Entry]

Name=example

Comment=My Python Program

Exec=python /home/pi/example.py

Icon=/home/pi/example.png

Terminal=false 
MultipleArgs=false 
Type=Application 
Categories=Application;Development; 
StartupNotify=true 



github的用法
上传文件
1.$ cd /D
2.$ git clone https://github.com/MissHjf/mygithub.git  
  mygithub为你在github网页上创建的仓库
  然后在D/mygithub中创建你需要的文件
3.$ cd /D/mygithub
4.$ ls
5.$ git add 你要上传的文件
6. git commit -m "cc"     ,cc用你要备注的内容代替
7.$ git push origin master

更新仓库里的文件
1.$ cd /D/mygithub
2.$ ls
3.$ git add 你要更新上传的文件
4.$ git commit -m "cc"     ,cc用你要备注的内容代替  （必须备注）
5.$ git pull origin master
6.如果过程中出现‘please enter a commit message…’,首先按下esc退出键然后输入 ：wq即可
7.$ git push -u origin master

修改备注的内容
1.$ cd /D/mygithub
2.$ git commit --amend
3.三个Enter
4.按键i可进入编辑模式
5.修改注释信息，然后退出编辑模式,按键ESC可退出编辑模式（与vim用法相同）
6.输入:wq（与vim用法相同）可保存退出。
7.$ git pull origin master
8.$ git push -u origin master
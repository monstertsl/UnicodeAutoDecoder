# UnicodeAutoDecoder

自动将抓包、重放、爆破中的Unicode编码准换为易于阅读的自然语言编码(UTF-8)  
Auto converts Unicode encodings in Proxy, Repeater, and Intruder into easy-to-read natural language

参考以下两个项目进行创建  
Refer to the following two authors create project  
https://github.com/amir-h-fallahi/UnicodeDecoder  
https://github.com/no001ce/N-DecodeAllUnicode  

因为一开始我使用的是[UnicodeDecoder](https://github.com/amir-h-fallahi/UnicodeDecoder),后面发现他会导致在重放和爆破的时候对请求/响应中的中文进行编码，导致无法正常阅读，所以在[UnicodeDecoder](https://github.com/amir-h-fallahi/UnicodeDecoder)的基础上，参照[N-DecodeAllUnicode](https://github.com/no001ce/N-DecodeAllUnicode)进行修改

# 使用方式
脚本使用python编写，需要先在BurpSuite中配置python环境，安装[Jython](https://www.jython.org/download.html)在Java环境中实现python
BurpSuite - Extensions(扩展) - Extensions settings(扩展设置) - Python environment（Python环境） - Location of Jython standalone JAR file（Jython的JAR文件位置） - Select file（选择文件）
选择下载好的[Jython](https://www.jython.org/download.html)
## 载入插件
BurpSuite - Extensions(扩展) - Installed（安装） - Burp extensions（Burp扩展） - Add（添加） - Extension type（扩展类型） - Python - Extension file - Select file（选择文件）
选择下载好的[UnicodeAutoDecoder](https://github.com/monstertsl/UnicodeAutoDecoder)


#测试URL
https://aiqicha.baidu.com/index/getCPlaceAjax
https://passport.baidu.com/v2/api/getqrcode

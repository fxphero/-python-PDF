# Save-links-in-wechat-as-pdf-python-
1 获取微信文章信息
  多选微信连接选择‘发送至邮件’，将邮件内容保存在txt中，根据微信版本不同，有两种txt文件：
  1.1 如果是7.0之前版本微信，txt内容应该是每个链接占两行，如：
    “
    小明 12：34：
    [‘标题示例1‘ ：’url示例1‘]
    
    小明 12：35：
    [‘标题示例2‘ ：’url示例2‘]
    ”
  1.2 如果是7.0之后版本微信，txt内容应该是一行字符串。
  请根据具体情况其中一个脚本。
  
2 程序依赖
  2.1 wkhtmltox软件
  2.2 pdfkit库

3 配置相关路径：
  source_path = r'D:/7-3.txt'    #这里是邮件txt位置
  save_path = r'D:/wxwz/'  #这里设置pdf保存位置
  wkhtmltopdf_path = r'D:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'   #这里设置wkhtmltox程序的路径
  
4 运行程序
  

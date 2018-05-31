
# from selenium import webdriver                  #从selenium库导入webdirver
from selenium.webdriver.chrome.options import Options
# import time
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
# url = 'https://detail.tmall.com/item.htm?spm=a1z10.4-b-s.w5003-15999627838.4.3e92d4b3qSKYOl&id=2252294794&scene=taobao_shop'
# browser = webdriver.Chrome(chrome_options=chrome_options)
# # = webdriver.PhantomJS(executable_path=)  
# #browser = webdriver.Chrome()              #使用webdirver.PhantomJS()方法新建一个phantomjs的对象，这里会使用到phantomjs.exe，环境变量path中找不到phantomjs.exe，则会报错

# browser.get(url)                                          #使用get()方法，打开指定页面。注意这里是phantomjs是无界面的，所以不会有任何页面显示
# browser.maximize_window()   #设置phantomjs浏览器全屏显示
# #print (browser.title) 
# #picName =    browser.title+'.jpg'  
# # js="var q=document.documentElement.scrollTop=6500"
# # browser.execute_script(js)    
# #time.sleep(5)        
# browser.save_screenshot('jj.jpg')           #使用save_screenshot将浏览器正文部分截图，即使正文本分无法一页显示完全，save_screenshot也可以完全截图
# browser.close()                 

from selenium import webdriver
import time

def take_screenshot(url, save_fn="capture.png"):
    #browser = webdriver.Firefox() # Get local session of firefox
    #browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = webdriver.PhantomJS(executable_path=r'.\phantomjs-2.1.1-windows\bin\phantomjs.exe',service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']) 
    browser.set_window_size(1500, 900)
    browser.get(url) # Load page
    # 点击账号密码登录
    # browser.execute_script("var q=document.find_element_by_id('J_Quick2Static');q.click()")
    # browser.implicitly_wait(3)
     
    # # 填写登录信息
    # browser.find_element_by_id('TPL_username_1').clear()
    # browser.find_element_by_id('TPL_username_1').send_keys('shuhuizhen0')
    # browser.find_element_by_id('TPL_password_1').clear()
    # browser.find_element_by_id('TPL_password_1').send_keys('y~m~k~0925')
     
    # # 登录
    # browser.execute_script("var login=document.getElementById('J_SubmitStatic');login.click();")
    # browser.implicitly_wait(3)
     
    # # 获取Cookie
    # cookie = browser.get_cookies()
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);

            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }

            setTimeout(f, 1000);
        })();
    """)

    for i in range(30):
        if "scroll-done" in browser.title:
            break
        time.sleep(10)

    browser.save_screenshot(save_fn)
    browser.close()
def date_time(delta):
	now = datetime.date.today()
	delta2 = datetime.timedelta(days=1)
	delta = datetime.timedelta(days=delta)
	n_days = now-delta2 - delta
	return (n_days.strftime('%Y-%m-%d'))

if __name__ == "__main__":
    import xlrd
    import datetime,os
    comment =  xlrd.open_workbook(r'test.xls')#(),encoding='utf-8',errors='ignore'
    table = comment.sheets()[0] 
    nrows = table.nrows
    ncols = table.ncols
    product = table.row_values(0)[1]
    filepath = '.\\'+product+'\\'+date_time(-1)+'\\'
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    for i in range(1,nrows):

        
        name = '.\\'+product+'\\'+date_time(-1)+'\\'+str(i)+table.row_values(i)[1]+'.png'
        url = table.row_values(i)[2]
        print (name)
        take_screenshot(url,name)


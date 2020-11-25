from urllib import request
from lxml import etree
#构造函数，抓取第i页信息
import xlwt
def crow(i):

    #  构造第i页的网址
    
        url='http://movie.douban.com/top250?start='+str(25*i)
        #  发送请求，获得返回的html代码并保存在变量html中
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68"
        }

        req = request.Request(url,headers=header)
        html=request.urlopen(req).read().decode('utf-8')
        #将返回的字符串格式的html代码转换成xpath能处理的对象
        html=etree.HTML(html)
        
        #先定位到li标签，datas是一个包含25个li标签的list，就是包含25部电影信息的list
        datas = html.xpath('//ol[@class="grid_view"]/li')
    # a=0
    
        for data in datas:
            
            data_title=data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')
            data_info=data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')
            data_quote=data.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()')
            data_score=data.xpath('div/div[2]/div[@class="bd"]/div/span[@class="rating_num"]/text()')
            data_num=data.xpath('div/div[2]/div[@class="bd"]/div/span[4]/text()')
            data_picurl=data.xpath('div/div[1]/a/img/@src')
    
            with open('douban250_1.csv','a',encoding='utf-8') as f:
                #封面图片保存路径和文件名
                f.write(data_title[0]+",")
                f.write(data_info[1].strip().replace(" ","")+",")
                # #因为发现有几部电影没有quote，所以这里加个判断，以免报错
                # # if data_quote:
                # #     f.write(data_quote[0]+'\n')
                f.write(data_score[0]+",")
                f.write(data_num[0])
                f.write("\n")
            # a+=1 
             
for i in range(10):
    crow(i)
#好吧，信息也有了，这个列表再想一下吧！明天重新试一下呗
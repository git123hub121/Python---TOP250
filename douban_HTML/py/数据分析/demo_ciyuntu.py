import jieba
import collections
import re
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts import options as opts
from pyecharts.globals import ThemeType, CurrentConfig
#用pyecharts画图必备四个模块
#先读取数据
with open("D:\Python\douban_HTML\一粒红尘评论.txt",encoding="utf-8") as f:
    data = f.read()
#匹配中文和整体读取，间接去除不相关字符   匹配中文：[\u4e00-\u9fa5]+
newdata = re.findall('[\u4e00-\u9fa5]+',data,re.S)#+表示前一个字符1次或无限次扩展   使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配
newdata = " ".join(newdata)#将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#文本分词
txt_split = jieba.cut(newdata,cut_all=True)#选择精准模式
#txt_split是一个可遍历对象

result_list = []
#选择停用词继续清理无关词语
with open("D:\Python\douban_HTML\停用词大全.txt",encoding="utf-8") as f:
    tyc = f.readlines()#读取所有行
    stop_words = set()#放入集合，进一步去重
    for i in tyc:
        i = i.replace("\n","")# 去掉读取每一行数据的\n
        stop_words.add(i)

#判断
for word in txt_split:
    if word not in stop_words and len(word) > 1:
        result_list.append(word)
#输出---测试
print(result_list)

#筛选统计top100
word_count = collections.Counter(result_list)
word_count_top100 = word_count.most_common(100)
print(word_count_top100)
#制作词云图
word1 = WordCloud(
    init_opts=opts.InitOpts(
        width='1350px', height='750px', theme=ThemeType.WONDERLAND,)
    )
word1.add('词频', data_pair=word_count_top100,
          word_size_range=[15, 108], textstyle_opts=opts.TextStyleOpts(font_family='cursive'),
          shape=SymbolType.DIAMOND)
word1.set_global_opts(title_opts=opts.TitleOpts('商品评论词云图'),
                      toolbox_opts=opts.ToolboxOpts(is_show=True, orient='vertical'),
                      tooltip_opts=opts.TooltipOpts(is_show=True, background_color='red', border_color='yellow'))
word1.render("商品评论词云图.html")
#暂不支持该写法
# cyt = (
#     .add(
#         '词频',
#         data_pair=word_count_top100,
#         word_size_range= [15,108],
#         textstyle_opts = opts.TextStyleOpts(font_family='cursive'),
#         shape=SymbolType.DIAMOND,
#         )
#     .set_global_opts(
#         title_opts=opts.TitleOpts('商品评论词云图'),
#         toolbox_opts=opts.ToolboxOpts(
#                 is_show=True, orient='vertical'),
#         tooltip_opts=opts.TooltipOpts(
#                 is_show=True, 
#                 background_color='red', 
#                 border_color='yellow'),
#         #显示工具栏
#         toolbox_opts=opts.ToolboxOpts(is_show=True),
#         )
#     .render("商品评论词云图.html")
# )

thm = '''
 |  CHALK = 'chalk' #粉笔风
 |  
 |  DARK = 'dark'  #暗黑风
 |  
 |  ESSOS = 'essos' #厄索斯大陆
 |  
 |  INFOGRAPHIC = 'infographic' #信息图
 |  
 |  LIGHT = 'light' #明亮风格
 |  
 |  MACARONS = 'macarons' #马卡龙
 |  
 |  PURPLE_PASSION = 'purple-passion' #紫色激情
 |  
 |  ROMA = 'roma' #石榴
 |  
 |  ROMANTIC = 'romantic' #浪漫风
 |  
 |  SHINE = 'shine' #闪耀风
 |  
 |  VINTAGE = 'vintage' #复古风
 |  
 |  WALDEN = 'walden' #瓦尔登湖
 |  
 |  WESTEROS = 'westeros' #维斯特洛大陆
 |  
 |  WHITE = 'white' #洁白风
 |  
 |  WONDERLAND = 'wonderland' #仙境
 '''







#Python高级数据结构-Collections模块
# a）Counter： 计数器，用于统计元素的数量
# b）OrderDict：有序字典
# c）defaultdict：值带有默认类型的字典
# d）namedtuple：可命名元组，通过名字来访问元组元素
# e）deque :双向队列，队列头尾都可以放，也都可以取
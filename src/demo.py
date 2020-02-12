#!/usr/bin/env python
# coding: utf-8

# # 新型冠状病毒数据分析演示
# 
# 新型冠状病毒（2019-nCov) 的疫情牵动着全世界人民的心，而理性地对待离不开数据和分析。为了让人民大众及时了解情况，很多网站都公布疫情的实时信息。比方说[丁香园疫情实时动态](https://ncov.dxy.cn/ncovh5/view/pneumonia)， [腾讯疫情实时追踪](https://news.qq.com/zt2020/page/feiyan.htm) 等等。这些网站的内容都是一样的，它们快速地为公众提供了信息，增加了透明度。但是如果读者希望对疫情有进一步的了解，这些网站就不够用了。比方说，如果你想得到过去十天湖北省确诊人数，那就只能从趋势图上作个估计了。再比方说，如果你想对比一下湖南、广东、浙江三省在过去十天的新增确诊人数，那么单凭网页数据也无能为力了。
# 
# 为了取得可以供研究使用的数据，[DXY-2019-nCoV-Data](https://github.com/BlankerL/DXY-2019-nCoV-Data) 项目利用网络爬虫不断从网上抓取数据，更新并存成 CSV 格式。然而，这个 CSV 文件包含的是不同时刻网页上的信息片段，有的时候只有这几个城市，有的时候只有那几个城市，数据并不规整。
# 
# 为了进一步方便用户进行研究，本项目[nCov2019_analysis](https://github.com/jianxu305/nCov2019_analysis) 提供了一些基本工具，把实时数据规整为每日数据，方便用户按时间、省份、城市等方法检索。同时，本项目还提供了基本的时间序列和横向分析作图函数，方便用户取得基本信息。
# 
# 以下是基本使用方法演示：

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import utils   # some convenient functions

# get_ipython().run_line_magic('load_ext', 'autoreload')
# get_ipython().run_line_magic('autoreload', '2')


# ## 1. 获取原始 CSV 数据

# In[6]:


# data = utils.load_chinese_data()


# In[10]:


def load_chinese_data2():
    data = pd.read_csv("../DXY-2019-nCoV-Data/csv/DXYArea.csv")
    data['updateTime'] = pd.to_datetime(data['updateTime'])  # original type of updateTime after read_csv is 'str'
    data['updateDate'] = data['updateTime'].dt.date    # add date for daily aggregation
    # display basic info
    print('最近更新于: ', data['updateTime'].max())
    print('数据日期范围: ', data['updateDate'].min(), 'to', data['updateDate'].max())
    print('数据条目数: ', data.shape[0])
    return data


# In[11]:


data = load_chinese_data2()


# In[12]:


data.head(3)  # 查看数据形式


# ## 2. 把实时数据整合成每日数据

# In[13]:


daily_frm = utils.aggDaily(data, clean_data=True)


# In[14]:


daily_frm.tail(3)


# #### 用 utils.add_dailyNew() 加入每日新增确诊、死亡、治愈人数

# In[15]:


daily_frm = utils.add_dailyNew(daily_frm)


# In[16]:


daily_frm[daily_frm['cityName'] == '武汉'][['confirmed', 'dailyNew_confirmed', 'dead', 'dailyNew_dead', 'cured', 'dailyNew_cured', 'updateDate']][:5]


# In[17]:


daily_frm.to_csv("data/daily.csv")

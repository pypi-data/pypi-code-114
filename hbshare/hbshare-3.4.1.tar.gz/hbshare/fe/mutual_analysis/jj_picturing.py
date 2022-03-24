import pandas as pd
from hbshare.fe.XZ import db_engine
from hbshare.fe.XZ import functionality


util=functionality.Untils()
hbdb=db_engine.HBDB()
localdb=db_engine.PrvFunDB().engine


def industry_pic(jjdm,jjjc,th1=0.5,th2=0.5):

    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from hbs_industry_property",con=localdb)['asofdate'][0]

    sql="SELECT * from hbs_industry_property where jjdm='{0}' and asofdate='{1}' "\
        .format(jjdm,latest_date)
    industry_p=pd.read_sql(sql,con=localdb).rename(columns={'cen_ind':'行业集中度',
                                                            'ratio_ind':'行业换手率',
                                                            'cen_theme':'主题集中度',
                                                            'ratio_theme':'主题换手率',
                                                            'industry_num':'行业暴露数',
                                                            'top5': '前五大行业',
                                                            })

    float_col_list=industry_p.columns.tolist()
    float_col_list.remove('jjdm')
    float_col_list.remove('asofdate')
    float_col_list.remove('前五大行业')


    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from hbs_industry_shift_property",con=localdb)['asofdate'][0]

    sql="SELECT * from hbs_industry_shift_property where jjdm='{0}' and asofdate='{1}' "\
        .format(jjdm,latest_date)
    industry_sp=pd.read_sql(sql,con=localdb).set_index('项目名').fillna(0)
    ind_sp_float_col_list=industry_sp.columns.tolist()
    ind_sp_float_col_list.remove('jjdm')
    ind_sp_float_col_list.remove('asofdate')

    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from hbs_theme_shift_property",con=localdb)['asofdate'][0]

    sql="SELECT * from hbs_theme_shift_property where jjdm='{0}' and asofdate='{1}' "\
        .format(jjdm,latest_date)
    theme_sp=pd.read_sql(sql,con=localdb).set_index('项目名').fillna(0)

    theme_sp_float_col_list=theme_sp.columns.tolist()
    theme_sp_float_col_list.remove('jjdm')
    theme_sp_float_col_list.remove('asofdate')




    #generate the label:
    if(industry_p['行业集中度'][0]>th1 and industry_p['行业换手率'][0]>th2):
        industry_p['行业类型']='博弈'
    elif(industry_p['行业集中度'][0]>th1 and industry_p['行业换手率'][0]<th2):
        industry_p['行业类型'] = '专注'
    elif(industry_p['行业集中度'][0]<th1 and industry_p['行业换手率'][0]>th2):
        industry_p['行业类型'] = '轮动'
    elif(industry_p['行业集中度'][0]<th1 and industry_p['行业换手率'][0]<th2):
        industry_p['行业类型'] = '配置'

    if(industry_p['主题集中度'][0]>th1 and industry_p['主题换手率'][0]>th2):
        industry_p['主题类型']='博弈'
    elif(industry_p['主题集中度'][0]>th1 and industry_p['主题换手率'][0]<th2):
        industry_p['主题类型'] = '专注'
    elif(industry_p['主题集中度'][0]<th1 and industry_p['主题换手率'][0]>th2):
        industry_p['主题类型'] = '轮动'
    elif(industry_p['主题集中度'][0]<th1 and industry_p['主题换手率'][0]<th2):
        industry_p['主题类型'] = '配置'


    for col in float_col_list:
        industry_p[col]=industry_p[col].map("{:.2%}".format)


    for col in ind_sp_float_col_list[0:int(len(ind_sp_float_col_list)/2)]:
        industry_sp.loc[industry_sp.index!='切换次数',col]=\
            industry_sp.iloc[1:][col].astype(float).map("{:.2%}".format)
    for col in ind_sp_float_col_list[int(len(ind_sp_float_col_list)/2):]:
        industry_sp[col]=\
            industry_sp[col].astype(float).map("{:.2%}".format)

    for col in theme_sp_float_col_list[0:int(len(theme_sp_float_col_list)/2)]:
        theme_sp.loc[theme_sp.index!='切换次数',col]=\
            theme_sp.iloc[1:][col].astype(float).map("{:.2%}".format)
    for col in theme_sp_float_col_list[int(len(theme_sp_float_col_list)/2):]:
        theme_sp[col]=\
            theme_sp[col].astype(float).map("{:.2%}".format)

    industry_p['基金简称']=[jjjc]


    theme_p=industry_p[['jjdm','基金简称','主题类型','主题集中度', '主题换手率','大金融', '消费', 'TMT',
       '周期', '制造', 'asofdate']]

    industry_p=industry_p[['jjdm','基金简称','行业类型','行业集中度', '行业换手率','前五大行业','国防军工',
       '农林牧渔', '汽车', '银行', '建筑装饰', '化工', '建筑材料', '商业贸易', '计算机', '综合', '电气设备',
       '电子', '食品饮料', '医药生物', '家用电器', '钢铁', '休闲服务', '轻工制造', '机械设备', '传媒', '采掘',
       '非银金融', '有色金属', '房地产', '通信', '纺织服装', '交通运输', '公用事业','asofdate']]

    industry_sp=industry_sp[['Total_rank', '国防军工_rank', '农林牧渔_rank', '汽车_rank', '银行_rank',
       '建筑装饰_rank', '化工_rank', '建筑材料_rank', '商业贸易_rank', '计算机_rank', '综合_rank',
       '电气设备_rank', '电子_rank', '食品饮料_rank', '医药生物_rank', '家用电器_rank',
       '钢铁_rank', '休闲服务_rank', '轻工制造_rank', '机械设备_rank', '传媒_rank', '采掘_rank',
       '非银金融_rank', '有色金属_rank', '房地产_rank', '通信_rank', '纺织服装_rank',
       '交通运输_rank', '公用事业_rank','Total', '国防军工', '农林牧渔', '汽车', '银行', '建筑装饰', '化工', '建筑材料', '商业贸易',
       '计算机', '综合', '电气设备', '电子', '食品饮料', '医药生物', '家用电器', '钢铁', '休闲服务', '轻工制造',
       '机械设备', '传媒', '采掘', '非银金融', '有色金属', '房地产', '通信', '纺织服装', '交通运输', '公用事业','asofdate']]
    industry_sp.reset_index(inplace=True)

    theme_sp=theme_sp[['Total_rank',
       '大金融_rank', '消费_rank', 'TMT_rank', '周期_rank', '制造_rank',
                       'Total', '大金融', '消费', 'TMT', '周期', '制造','asofdate']]
    theme_sp.reset_index(inplace=True)

    return industry_p,industry_sp,theme_p,theme_sp


def style_pic(jjdm,jjjc,fre,th1=0.5,th2=0.5):

    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from nav_style_property_value where fre='{0}'"
            .format(fre),con=localdb)['asofdate'][0]

    sql="SELECT * from nav_style_property_value where jjdm='{0}' and fre='{1}' and asofdate='{2}' "\
        .format(jjdm,fre,latest_date)
    value_p=pd.read_sql(sql,con=localdb).rename(columns={'shift_ratio_rank':'换手率排名',
                                                         'centralization_rank':'集中度排名',
                                                         '成长_mean':'成长暴露排名',
                                                         '价值_mean':'价值暴露排名',
                                                         'manager_change':'是否有过经理变更',
                                                         'shift_ratio':'换手率',
                                                         'centralization':'集中度',
                                                         'fre':'回归周期',
                                                         })

    # generate the label:
    winning_value=value_p[['成长暴露排名','价值暴露排名']].T[value_p[['成长暴露排名','价值暴露排名']].T[0]
                                                 ==value_p[['成长暴露排名','价值暴露排名']].T.max()[0]].index[0]
    if(value_p['集中度排名'][0]>th1 and value_p['换手率排名'][0]>th2 ):
        value_p['风格类型']='博弈'
        value_p['风格偏好']=winning_value[0:2]
    elif(value_p['集中度排名'][0]>th1 and value_p['换手率排名'][0]<th2 ):
        value_p['风格类型'] = '专注'
        value_p['风格偏好'] = winning_value[0:2]
    elif(value_p['集中度排名'][0]<th1 and value_p['换手率排名'][0]>th2 ):
        value_p['风格类型'] = '轮动'
        value_p['风格偏好'] = '均衡'
    elif(value_p['集中度排名'][0]<th1 and value_p['换手率排名'][0]<th2 ):
        value_p['风格类型'] = '配置'
        value_p['风格偏好'] =  '均衡'



    value_p['基金简称']=jjjc
    value_p=value_p[['jjdm','基金简称','风格类型','风格偏好','换手率排名','集中度排名',
                     '成长暴露排名', '价值暴露排名', '是否有过经理变更',
                     '换手率', '集中度','回归周期','asofdate']]



    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from nav_style_property_size where fre='{0}'"
            .format(fre),con=localdb)['asofdate'][0]

    sql="SELECT * from nav_style_property_size where jjdm='{0}' and fre='{1}' and asofdate='{2}' "\
        .format(jjdm,fre,latest_date)
    size_p=pd.read_sql(sql,con=localdb).rename(columns={'shift_ratio_rank':'换手率排名',
                                                         'centralization_rank':'集中度排名',
                                                         '大盘_mean':'大盘暴露排名',
                                                         '中盘_mean':'中盘暴露排名','小盘_mean':'小盘暴露排名',
                                                         'manager_change':'是否有过经理变更',
                                                         'shift_ratio':'换手率',
                                                         'centralization':'集中度',
                                                         'fre':'回归周期',
                                                         })

    # generate the label:
    winning_size=[x[0] for x in size_p[['大盘暴露排名','中盘暴露排名','小盘暴露排名']].T[size_p[['大盘暴露排名','中盘暴露排名','小盘暴露排名']].T[0]>0.5].index.tolist()]
    winning_size=''.join(winning_size)

    if(size_p['集中度排名'][0]>th1 and size_p['换手率排名'][0]>th2 ):
        size_p['规模风格类型']='博弈'
        size_p['规模偏好']=winning_size
    elif(size_p['集中度排名'][0]>th1 and size_p['换手率排名'][0]<th2 ):
        size_p['规模风格类型'] = '专注'
        size_p['规模偏好'] = winning_size
    elif(size_p['集中度排名'][0]<th1 and size_p['换手率排名'][0]>th2 ):
        size_p['规模风格类型'] = '轮动'
        size_p['规模偏好'] = '均衡'
    elif(size_p['集中度排名'][0]<th1 and size_p['换手率排名'][0]<th2 ):
        size_p['规模风格类型'] = '配置'
        size_p['规模偏好'] ='均衡'

    size_p['基金简称']=jjjc
    size_p=size_p[['jjdm','基金简称','规模风格类型','规模偏好','换手率排名','集中度排名','大盘暴露排名', '中盘暴露排名','小盘暴露排名', '是否有过经理变更',
                     '换手率', '集中度','回归周期','asofdate']]



    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from nav_shift_property_value where fre='{0}'"
            .format(fre),con=localdb)['asofdate'][0]

    sql="SELECT * from nav_shift_property_value where jjdm='{0}' and asofdate='{1}' and fre='{2}' "\
        .format(jjdm,latest_date,fre)
    value_sp=pd.read_sql(sql,con=localdb).set_index('项目名').fillna(0)
    value_sp_float_col_list=value_sp.columns.tolist()
    value_sp_float_col_list.remove('jjdm')
    value_sp_float_col_list.remove('asofdate')
    value_sp_float_col_list.remove('fre')



    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from nav_shift_property_size where fre='{0}'"
            .format(fre),con=localdb)['asofdate'][0]

    sql="SELECT * from nav_shift_property_size where jjdm='{0}' and asofdate='{1}' and fre='{2}' "\
        .format(jjdm,latest_date,fre)
    size_sp=pd.read_sql(sql,con=localdb).set_index('项目名').fillna(0)
    size_sp_float_col_list=size_sp.columns.tolist()
    size_sp_float_col_list.remove('jjdm')
    size_sp_float_col_list.remove('asofdate')
    size_sp_float_col_list.remove('fre')


    for col in ['换手率排名', '集中度排名', '成长暴露排名', '价值暴露排名',
                       '换手率', '集中度', ]:
        value_p[col]=value_p[col].map("{:.2%}".format)

    for col in ['换手率排名', '集中度排名', '大盘暴露排名', '中盘暴露排名','小盘暴露排名',
                       '换手率', '集中度', ]:
        size_p[col]=size_p[col].map("{:.2%}".format)


    for col in ['Total', '成长', '价值']:
        value_sp.loc[value_sp.index!='切换次数',col]=\
            value_sp.iloc[1:][col].astype(float).map("{:.2%}".format)
    for col in ['Total_rank', '成长_rank', '价值_rank']:
        value_sp[col]=\
            value_sp[col].astype(float).map("{:.2%}".format)

    for col in ['Total', '大盘', '中盘', '小盘']:
        size_sp.loc[size_sp.index!='切换次数',col]=\
            size_sp.iloc[1:][col].astype(float).map("{:.2%}".format)
    for col in ['Total_rank', '大盘_rank', '中盘_rank', '小盘_rank']:
        size_sp[col]=\
            size_sp[col].astype(float).map("{:.2%}".format)


    value_sp=value_sp[['Total_rank', '成长_rank', '价值_rank',
                       'Total', '成长', '价值','fre','asofdate']]
    size_sp = size_sp[['Total_rank','大盘_rank', '中盘_rank',
       '小盘_rank','Total', '大盘', '中盘', '小盘','fre','asofdate']]

    value_sp.reset_index(inplace=True)
    size_sp.reset_index(inplace=True)


    return  value_p,value_sp,size_p,size_sp


def stock_trading_pci(jjdm,jjjc,ind_cen,th1=0.75,th2=0.25,th3=0.5,th4=0.5,th5=0.75,th6=0.5):

    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from hbs_holding_property "
        ,con=localdb)['asofdate'][0]

    sql="SELECT * from hbs_holding_property where jjdm='{0}' and asofdate='{1}' "\
        .format(jjdm,latest_date)
    stock_p=pd.read_sql(sql,con=localdb)

    float_col=stock_p.columns.tolist()
    float_col.remove('jjdm')
    float_col.remove('asofdate')
    float_col.remove('持股数量')
    float_col.remove('PE')
    float_col.remove('PB')
    float_col.remove('ROE')
    float_col.remove('股息率')
    float_col.remove('PE_中位数')
    float_col.remove('PB_中位数')
    float_col.remove('ROE_中位数')
    float_col.remove('股息率_中位数')


    latest_date=pd.read_sql(
        "select max(asofdate) as asofdate from hbs_stock_trading_property "
        ,con=localdb)['asofdate'][0]

    sql="SELECT * from hbs_stock_trading_property where jjdm='{0}' and asofdate='{1}' "\
        .format(jjdm,latest_date)
    stock_tp=pd.read_sql(sql,con=localdb)

    tp_float_col=stock_tp.columns.tolist()
    tp_float_col.remove('jjdm')
    tp_float_col.remove('平均持有时间（出重仓前）')
    tp_float_col.remove('平均持有时间（出持仓前）')
    tp_float_col.remove('asofdate')


    #generate the labels

    if(stock_p['个股集中度'][0]>th1 and stock_tp['平均持有时间（出持仓前）_rank'][0]>th1 ):
        stock_p['个股风格A']='专注'
    elif(stock_p['个股集中度'][0]>th1 and stock_tp['平均持有时间（出持仓前）_rank'][0]<th2 ):
        stock_p['个股风格A'] = '博弈'
    elif(stock_p['个股集中度'][0]<th2 and stock_tp['平均持有时间（出持仓前）_rank'][0]>th1 ):
        stock_p['个股风格A'] = '配置'
    elif(stock_p['个股集中度'][0]<th2 and stock_tp['平均持有时间（出持仓前）_rank'][0]<th2 ):
        stock_p['个股风格A'] = '轮动'
    else:
        stock_p['个股风格A'] = '无'


    if(stock_p['个股集中度'][0]>th1 and ind_cen<th6 ):
        stock_p['个股风格B']='自下而上'
    elif(stock_p['个股集中度'][0]<th6 and ind_cen>th1 ):
        stock_p['个股风格B'] = '自上而下'

    else:
        stock_p['个股风格B'] = '无'

    if(stock_p['个股集中度'][0]>th1 and stock_p['个股集中度'][0]-stock_p['hhi'][0]>0.05):
        stock_p['是否有尾仓(针对高个股集中基金）']='有尾仓'
    else:
        stock_p['是否有尾仓(针对高个股集中基金）'] = '无尾仓'

    if(stock_tp['左侧概率（出持仓前,半年线）_rank'][0]>th3 and stock_tp['左侧程度（出持仓前,半年线）'][0]>th4):
        stock_tp['左侧标签']='深度左侧'
    elif(stock_tp['左侧概率（出持仓前,半年线）_rank'][0]>th3 and stock_tp['左侧程度（出持仓前,半年线）'][0]<th4):
        stock_tp['左侧标签'] = '左侧'
    else:
        stock_tp['左侧标签'] = '无'

    lable=''
    if(stock_tp['新股概率（出持仓前）_rank'][0]>th5):
        lable=+'偏好新股'
    if( stock_tp['次新股概率（出持仓前）_rank'][0]>th5):
        lable=+'偏好次新股'
    stock_tp['新股次新股偏好']=lable



    for col in float_col:
        stock_p[col]= stock_p[col].map("{:.2%}".format)
    for col in tp_float_col:
        stock_tp[col] = stock_tp[col].map("{:.2%}".format)



    stock_p['基金简称'] = jjjc
    stock_tp['基金简称'] = jjjc

    stock_p=stock_p[['jjdm','基金简称','个股风格A','个股风格B','是否有尾仓(针对高个股集中基金）','个股集中度', 'hhi','持股数量',
                     '前三大', '前五大', '前十大', '平均仓位', '仓位换手率','PE_rank', 'PB_rank', 'ROE_rank', '股息率_rank', 'PE_中位数_rank',
       'PB_中位数_rank', 'ROE_中位数_rank', '股息率_中位数_rank','PE', 'PB', 'ROE', '股息率',
                     'PE_中位数', 'PB_中位数', 'ROE_中位数', '股息率_中位数','asofdate'
                     ]]
    stock_tp=stock_tp[['jjdm','基金简称','左侧标签', '新股次新股偏好','左侧概率（出重仓前,半年线）_rank', '左侧概率（出持仓前,半年线）_rank',
       '左侧概率（出重仓前,年线）_rank', '左侧概率（出持仓前,年线）_rank',
                       '平均持有时间（出重仓前）_rank', '平均持有时间（出持仓前）_rank','出重仓前平均收益率_rank',
       '出全仓前平均收益率_rank',
                       '新股概率（出重仓前）_rank','新股概率（出持仓前）_rank', '次新股概率（出重仓前）_rank', '次新股概率（出持仓前）_rank','平均持有时间（出重仓前）', '平均持有时间（出持仓前）', '出重仓前平均收益率', '出全仓前平均收益率',
       '左侧概率（出重仓前,半年线）', '左侧概率（出持仓前,半年线）', '左侧概率（出重仓前,年线）', '左侧概率（出持仓前,年线）',
       '左侧程度（出重仓前,半年线）', '左侧程度（出持仓前,半年线）', '左侧程度（出重仓前,年线）', '左侧程度（出持仓前,年线）',
       '新股概率（出重仓前）', '新股概率（出持仓前）', '次新股概率（出重仓前）', '次新股概率（出持仓前）','asofdate'
                       ]]

    return stock_p,stock_tp




jjdm='005775'
jjjc=hbdb.db2df("select jjjc from st_fund.t_st_gm_jjxx where jjdm='{0}'".format(jjdm),db='funduser')['jjjc'][0]


value_p,value_sp,size_p,size_sp=style_pic(jjdm,jjjc,fre='M')
industry_p,industry_sp,theme_p,theme_sp=industry_pic(jjdm,jjjc)
stock_p,stock_tp=stock_trading_pci(jjdm,jjjc,ind_cen=float(industry_p['行业集中度'][0].split('%')[0])/100)


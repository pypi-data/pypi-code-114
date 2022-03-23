# encoding: UTF-8
import random

from ipygo.ftbase import *


########################################################################
class FTA(FTBase):
    """EGOPY定制策略模板"""
    if 1 > 0:
        className = 'FTA'
        author = u'EGOPY'
        # name = EMPTY_UNICODE  # 策略实例名称

        # 参数列表，保存了参数的名称
        paramList = ['r',
                     'x',
                     'maxL',
                     'maxS',
                     'posL',
                     'posS']

        # 变量列表，保存了变量的名称
        varList = ['trading',
                   'excTimes',
                   'posL',
                   'costL',
                   'posS',
                   'costS',
                   'model']

        # 参数映射表
        paramMap = {'r': u'尺度',
                    'x': u'X值',
                    'maxL': u'限仓L',
                    'maxS': u'限仓S',
                    'posL': u'接管L',
                    'posS': u'接管S',
                    'exchange': u'交易所',
                    'vtSymbol': u'合约代码'}

        # 变量映射表
        varMap = {'trading': u'交易',
                  'excTimes': u'次数',
                  'posL': u'L持仓',
                  'costL': u'L价格',
                  'posS': u'S持仓',
                  'costS': u'S价格',
                  'model': u'模型序列'}

    # ----------------------------------------------------------------------
    def __init__(self, ctaEngine=None, setting={}):
        """Constructor"""
        super().__init__(ctaEngine, setting)

        """深度设置环节，请慎重修改"""
        # self.vol = 1

    # -----------------------------------------------------------------------
    def onBar(self, bar):
        """收到Bar推送（必须由用户继承实现）"""
        trade_time = 1
        """交易时间锁定/tick时间校验"""
        if trade_time > 0:
            hour = bar.datetime.hour
            minute = bar.datetime.minute
            if hour < 9:
                self.output(u'out of time @ 9:00')
                self.startdt = datetime.datetime.now()
                return
            if hour == 13 and minute <= 30:
                self.output(u'out of time @ 13:30')
                self.startdt = datetime.datetime.now()
                return
            if hour == 14 and minute >= 58:
                self.output(u'out of time @ 14:58')
                return
            if 15 <= hour < 21:
                self.output(u'out of time @ 15~21')
                self.startdt = datetime.datetime.now()
                return
            if self.tick is None:
                self.startdt = datetime.datetime.now()
                self.output(u'非预期交易时段: tick is None， start time {} '.format(self.startdt))
                return

        # time.sleep(random.randint(1, 100)/10)
        time.sleep(round(random.uniform(1, 10), 2))

        super().onBar(bar)
        self.model = u'{}#{}.{}#{}.{}#{}'.format(self.name, self.r, self.x, self.maxL, self.maxS, self.y)

    # ----------------------------------------------------------------------
    def execSignal(self):
        """交易信号执行"""
        self.output('\n 你找对地方了吗？ \n 自定义代码写在此处！')
        """新执行策略写在此处"""

    # ----------------------------------------------------------------------
    def onStart(self):
        # 注意交易所筛选
        super().onStart()

        # DemoK test
        self.output(u'\n 实例编号 ~ {}'.format(self.model))
        self.output(u'合约: {} - {} 交易所 \n'.format(self.vtSymbol, self.exchange))

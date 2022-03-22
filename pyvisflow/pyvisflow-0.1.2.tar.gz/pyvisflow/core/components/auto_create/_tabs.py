from typing import Union,Dict,List
from pyvisflow.core.components.containers import Container
from pyvisflow.core.props import TypePropInfo,StrTypePropInfo,SubscriptableTypePropInfo, NumberTypePropInfo, BoolTypePropInfo
from pyvisflow.models.TComponent import TComponentType
from pyvisflow.core.props import *


class _Tabs(Container):
    '''
    分隔内容上有关联但属于不同类别的数据集合
    '''

    def __init__(self) -> None:
        super().__init__('tabs', TComponentType.builtIn)

    def _ex_get_react_data(self):
        return super()._ex_get_react_data()


    @property
    def names(self):
        '''
        可选值：nan \n
        选项卡名字
        '''

        
        p = self.get_prop('names')
        return SubscriptableTypePropInfo[int,StrTypePropInfo](p)

        


    @names.setter
    def names(self, value: Union[SubscriptableTypePropInfo[int,StrTypePropInfo],List[str]]):
        '''
        可选值：nan \n
        选项卡名字
        '''
        self.set_prop('names', value)

    @property
    def activeName(self):
        '''
        可选值：nan \n
        当前激活的选项卡名字
        '''

        
        p = self.get_prop('activeName')
        return StrTypePropInfo(p)

        


    @activeName.setter
    def activeName(self, value: Union[StrTypePropInfo,str]):
        '''
        可选值：nan \n
        当前激活的选项卡名字
        '''
        self.set_prop('activeName', value)

    @property
    def value(self):
        '''
        可选值：nan \n
        绑定值，选中选项卡的 name
        '''

        
        p = self.get_prop('value')
        return StrTypePropInfo(p)

        


    @value.setter
    def value(self, value: Union[StrTypePropInfo,Union[str,float]]):
        '''
        可选值：nan \n
        绑定值，选中选项卡的 name
        '''
        self.set_prop('value', value)

    @property
    def type(self):
        '''
        可选值：card/border-card \n
        风格类型
        '''

        
        p = self.get_prop('type')
        return StrTypePropInfo(p)

        


    @type.setter
    def type(self, value: Union[StrTypePropInfo,str]):
        '''
        可选值：card/border-card \n
        风格类型
        '''
        self.set_prop('type', value)

    @property
    def closable(self):
        '''
        可选值：card/border-card \n
        标签是否可关闭
        '''

        
        p = self.get_prop('closable')
        return BoolTypePropInfo(p)

        


    @closable.setter
    def closable(self, value: Union[BoolTypePropInfo,bool]):
        '''
        可选值：card/border-card \n
        标签是否可关闭
        '''
        self.set_prop('closable', value)

    @property
    def addable(self):
        '''
        可选值：card/border-card \n
        标签是否可增加
        '''

        
        p = self.get_prop('addable')
        return BoolTypePropInfo(p)

        


    @addable.setter
    def addable(self, value: Union[BoolTypePropInfo,bool]):
        '''
        可选值：card/border-card \n
        标签是否可增加
        '''
        self.set_prop('addable', value)

    @property
    def editable(self):
        '''
        可选值：card/border-card \n
        标签是否同时可增加和关闭
        '''

        
        p = self.get_prop('editable')
        return BoolTypePropInfo(p)

        


    @editable.setter
    def editable(self, value: Union[BoolTypePropInfo,bool]):
        '''
        可选值：card/border-card \n
        标签是否同时可增加和关闭
        '''
        self.set_prop('editable', value)

    @property
    def tab_position(self):
        '''
        可选值：top/right/bottom/left \n
        选项卡所在位置
        '''

        
        p = self.get_prop('tab-position')
        return StrTypePropInfo(p)

        


    @tab_position.setter
    def tab_position(self, value: Union[StrTypePropInfo,str]):
        '''
        可选值：top/right/bottom/left \n
        选项卡所在位置
        '''
        self.set_prop('tab-position', value)

    @property
    def stretch(self):
        '''
        可选值：top/right/bottom/left \n
        标签的宽度是否自撑开
        '''

        
        p = self.get_prop('stretch')
        return BoolTypePropInfo(p)

        


    @stretch.setter
    def stretch(self, value: Union[BoolTypePropInfo,bool]):
        '''
        可选值：top/right/bottom/left \n
        标签的宽度是否自撑开
        '''
        self.set_prop('stretch', value)

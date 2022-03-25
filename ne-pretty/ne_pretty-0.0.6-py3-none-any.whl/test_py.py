# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 14:39
# @Author  : wyw

from ne_pretty import e_add_context
from ne_pretty import e_add_rule_context
from ne_pretty import e_do_connect
from ne_pretty import e_extend_prefix
from ne_pretty import e_extend_suffix
from ne_pretty import e_remove_prefix
from ne_pretty import e_remove_suffix

from ne_pretty import e_remove_contain
from ne_pretty import e_remove_eq
from ne_pretty import e_remove_dup
from ne_pretty import entity_diff


filename = r'C:\Users\acer\Desktop\demo\text.txt'

e_add_rule_context(filename,filename,'地点','(北京)')

#e_add_context(filename,filename,'地点','北京')


#e_remove_eq(filename,filename,'地点','北京')


#e_remove_suffix(filename,filename,'地点','北京')

#e_remove_prefix(filename,filename,'地点','北京')


#e_remove_contain(filename,filename,'作案手段')

#e_remove_dup(filename,filename)

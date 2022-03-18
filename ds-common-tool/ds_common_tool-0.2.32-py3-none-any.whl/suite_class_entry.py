from enum import Enum
from ds_common_tool.suite_sg_short import PriceForecastSGShort
from ds_common_tool.suite_shandong import PriceForecastShanDong

class ENV(Enum):
  LOCAL_TEST = 'localtest'
  EAP = 'eap'

class SuitePrice():
  def __init__(self, case_name, env = ENV.LOCAL_TEST.value):
    self.case_name = case_name
    self.env = env
    self.obj = None
    
  def get_obj(self):
    if self.case_name == 'usep':
      self.obj = PriceForecastSGShort(self.case_name, self.env)
    if self.case_name == 'eap':
      self.obj = PriceForecastShanDong(self.case_name, self.env)
    return self.obj
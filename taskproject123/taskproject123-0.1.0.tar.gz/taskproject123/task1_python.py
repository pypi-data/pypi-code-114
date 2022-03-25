from datetime import datetime
class Dummy():
  def __init__(self,bias,baseline=float(1/3)):
    self._bias=bias
    self._baseline=baseline

  @property          #read only -property decorator
  def bias(self):
    return self._bias

  @property          #read only -property decorator
  def baseline(self):
    return self._baseline

  @baseline.setter   #property-baseline.setter decorator
  def baseline(self, value):
    self.__baseline = value

  def multiplier_fun(self,multiplier):
    result=round(multiplier*self._baseline+self._bias,3)
    return result

  def time(self):
    now = datetime.utcnow()
    return " ".join(str(now).split()[::-1])
    
""" Bar chart """
import json
from .alignment import ChartAlignment
from .exceptions import ChartException
from .serie import ChartDataSerie
from .serie_type import ChartDataSerieType

class BarChart:
  """
  Bar chart configuration

  """

  def __init__(self, x_axis, y_axis, title='Chart', align=ChartAlignment.CENTER):
    """
    Constructor

    Args
    ----
      x_axis ChartDataSerie: Defines the X Axis of the chart, uses the ChartDataSerie class. Please read the documentation to more information.
      y_axis list(ChartDataSerie): Defines the Y Axis of the chart, uses the ChartDataSerie class. Please read the documentation to more information.
      title (str): Title of the chart
      align (ChartAlignment): Alignment of the title
    """
    for i, serie in enumerate(y_axis):
      if not isinstance(serie, ChartDataSerie):
        raise ChartException(f'Y Axis serie {i} must be an instance of ChartDataSerie')
    self.__y_axis = y_axis

    if not isinstance(x_axis, ChartDataSerie):
      raise ChartException('X Axis must be an instance of ChartDataSerie')
    self.__x_axis = x_axis

    if not isinstance(title, str):
      raise ChartException('title must be an instance of str')
    self.__title = title

    if not isinstance(align, ChartAlignment):
      raise ChartException('align must be an instance of ChartAlignment')
    self.__align = align

  @property
  def x_axis(self):
    """ X Axis of the chart """
    return self.__x_axis

  @property
  def y_axis(self):
    """ Y Axis of the chart """
    return self.__y_axis

  @property
  def title(self):
    """ Title of the chart """
    return self.__title

  def render(self):
    """
    Render chart to a Javascript Library.

    With less than 10.000 points (in X Axis), will return ApexCharts configuration. Else will return Google Charts
    """

    if len(self.y_axis) >= 1:
      return {
        'library': 'APEXCHARTS',
        'configuration': self.__render_apexcharts(len(self.y_axis[0].data) * len(self.y_axis) > 9_000)
      }

    return {
      'library': 'APEXCHARTS',
      'configuration': self.__render_apexcharts()
    }

  def __render_apexcharts(self, large_dataset=False):
    """
    Converts the configuration of the chart to Javascript library ApexCharts.
    """

    series = []
    colors = []

    for serie in self.__y_axis:
      modified_serie = {
        'name': serie.label,
        'data': serie.data
      }

      if serie.serie_type is not ChartDataSerieType.NONE:
        modified_serie['type'] = serie.serie_type.value

      series.append(modified_serie)
      colors.append(serie.color)

    config = {
      'series': series,
      'colors': colors,
      'xaxis': {
        'categories': self.__x_axis.data,
        'type': self.__x_axis.data_type.value,
        'title': {
          'text': self.__x_axis.label
        }
      },
      'title': {
        'text': self.__title,
        'align': self.__align.value
      },
      'plotOptions': {
        'bar': {
          'horizontal': True,
          'borderRadius': 4
        }
      },
      'dataLabels': {
        'enabled': not large_dataset
      },
      'chart': {
        'type': 'bar',
        'animations': {
          'enabled': False
        },
        'toolbar': {
          'show': False
        },
        'zoom': {
          'enabled': False
        }
      }
    }

    return config
import time
import logging
import traceback
import functools
import os
import typing
import wrapt
import tqdm
import requests

logger = logging.getLogger('dao')
logger.setLevel(logging.WARNING)

logger_debug = logger.debug
logger_info = logger.info
logger_warn = logger.warning
logger_error = logger.error

TMP_PATH_CACHE = 'tmp_cache'


def save_cache_to_file(if_read_cache_key=None):
    """加上装饰器就会保存函数结果到文件，装饰器设置if_read_cache_key字符床，函数定义时设置对应名称参数，并在调用时设置True可从文件读cache"""
    if if_read_cache_key and not os.path.exists(TMP_PATH_CACHE):
        os.makedirs(TMP_PATH_CACHE)

    @wrapt.decorator
    def wrapper(func, _instance, args, kwargs):
        cache_path = os.path.join(TMP_PATH_CACHE, func.__name__)
        if isinstance(if_read_cache_key, str) and kwargs.get(if_read_cache_key) and os.path.exists(cache_path):
            with open(cache_path, 'rb') as f:
                result = f.read()
            logger_info('[{}]函数读取到缓存: {} | {} | {}'.format(
                func.__name__, os.path.realpath(cache_path)[:-len(cache_path)], cache_path, repr(result)[:30]))
        else:
            result = func(*args, **kwargs)
            if result:
                with open(cache_path, 'wb') as f:
                    f.write(result)
                    logger_debug('[{}]函数结果缓存到: {} | {} |'.format(
                        func.__name__, os.path.realpath(cache_path)[:-len(cache_path)], cache_path))
        return result

    return wrapper


def pass_ex(if_ex_return=None, exs=None):
    """加上装饰器就会捕获所有异常，异常返回if_ex_return，exs中的异常会对应打印error，不再exs里面则打印堆栈信息"""
    if not exs:
        exs = {
            requests.exceptions.ConnectionError: '[ConnectionError] 代理失效或URL失效',
            requests.exceptions.ConnectTimeout: '[ConnectTimeout] 连接握手超时',
            requests.exceptions.ReadTimeout: '[ReadTimeout] 读取数据过程中超时',
        }

    @wrapt.decorator
    def wrapper(func, _instance, args, kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            if type(ex) in exs:
                logger_warn('{} {} 将返回  {}'.format(exs[type(ex)], func.__name__, repr(if_ex_return)))
            else:
                logger_warn("[{}] {} {}\n{}".format(type(ex), ex, func.__name__, traceback.format_exc()))
            return if_ex_return

    return wrapper


class Dao(object):
    """
    道、法、术、器、势、志
    道生一(志),一生二(法、术),二生三（器）,三生（势）万物
    # 道生一(志),一生二(势、法),二生三（术）,三生万物???

    志：产生类要达到的目的
    势： 函数生产者
    法： 函数如何调度消费者的方法，汇聚结果
    术： 消费者具体实现处理逻辑
    器： 消费者载体（进程、线程、函数、属性等）
    万物： 每个消费者产生的函数结果

    道：就是核心思想、理念、本质规律。很多时候有人纠结是自然规律，还是人定的思想，其实王阳明早说了“天理即人心”，我说“天理因人而存在”。这六个字，完全是因为人类存在而存在的，包括外星人。
    法：就是法律、规章、制度、方法。是以“道”为基础制定的不可违背的原则，比如有些经常挂在嘴边却不知所云的“大道自然”或者“以人为本”。
    术：行为与技巧，是可以以道为原则，做出反应和选择的，是以“道”为指导原则的。即“以道御术”，出自老子的《道德经》，很多人把“御”翻译成“承载”，实际上更贴切的是“驾驭”。以联想企业文化为例，联想提出“如果遇到公司没有相关规定的事，就按‘企业文化’办！”，这就是以道御术。
    器：是指工具，比如桌椅板凳或者企业里的打卡机，还有EXCEL管理表格之类的。总之“器”用来体现道的思想，是人体器官的延伸，从而简化问题，更快达成目标，是体现“器以载道”的应用。
    势：是从“道、法、术、器”体现的势能，比如“军魂、班风”之类的气场、气势、执行力。这个在“图1”里表现的是一个圈，其实画出来更应该像是太阳的光芒一样，感觉的到，摸 不到。以某个人为例，状态可以达到“善、诚、美、大、圣、神”的六重境界，善为别人以为你拥有美德，诚为你确实有美德，充盈为美，溢出为大，影响数个时代，众人为圣。影响千秋万代不同民族为神，比如佛教、基督教、伊斯兰教的创始人。
    志：主要是指目标，只有通过势能才能达到，势就是火箭助推器形成的力量。
    """

    # show_process = tqdm.tqdm
    show_process = iter

    def __init__(
            self, shi_func=None,
            shu_func=None,
            fa_func: typing.Union[list, iter, typing.Callable, None] = list,
            *args, **kwargs
    ):
        """

        :param shi_func: 函数生产者
        :param shu_func:
        :param fa_func:
        :param args:
        :param kwargs:
        """
        self.args = args
        self.kwargs = kwargs
        self.san = None
        self.wan_wu = None
        self.wan_wu_num_all = 0
        self.wan_wu_num_err = 0
        if shi_func:
            self.shi_func = shi_func
        if shu_func:
            self.shu_func = shu_func
        self.fa_func = fa_func  # for循环 map
        self.wd = self.wu_dao
        self.WD = self.wu_dao

    def wu_dao(
            self,
            shi_func=list,
            shu_func=None,
            fa_func: typing.Union[list, iter, typing.Callable, None] = list, *args: typing.Any, **kwargs: typing.Any):
        # 万物之道
        return self.__class__(shi_func, shu_func, fa_func, self.zhi(*args, **kwargs).wan_wu)

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return self.zhi(*args, **kwargs).wan_wu

    def qi_func(self, *args, **kwargs):
        """
        消费者载体 “器以载道”（用进程、线程、函数、属性等）
        :param args:
        :param kwargs:
        :return:
        """
        return self.shu_func(*args, **kwargs)

    def shu_func(self, dao):
        """
        消费者具体实现处理逻辑 filter print sum
        :param dao:
        :return:
        """
        self.wan_wu_num_all += 1
        logger_debug(f"{self.wan_wu_num_all}/{self.wan_wu_num_err}: {dao}")
        return dao

    def zhi(self, *args, **kwargs):
        start_time = time.time()
        logger_info('[开始] 生产 [{}()] {}'.format(
            self.shi_func.__name__ if hasattr(self.shi_func, '__name__') else self.shi_func,
            ('新参数', args, kwargs, '固定参数', self.args, self.kwargs)))
        if args or kwargs:
            self.args, self.kwargs = args, kwargs
        self.san = self.shi_func(*self.args, **self.kwargs)

        if self.fa_func is list:
            self.wan_wu = self.for_do_list(self.qi_func, self.san)
        elif self.fa_func is iter:
            self.wan_wu = self.for_do_iter(self.qi_func, self.san)
        elif callable(self.fa_func):
            self.wan_wu = self.fa_func(self.qi_func, self.san)
        else:
            raise NotImplemented
        logger_info('[{:.1f}s] 生产 [{}()] {} {}'.format(
            time.time() - start_time,
            self.shi_func.__name__ if hasattr(self.shi_func, '__name__') else self.shi_func,
            ('新参数', args, kwargs, '固定参数', self.args, self.kwargs), repr(self.san)[:50]))
        return self

    @classmethod
    def for_do_iter(cls, func, its, log_size=1, log_re=1000, timeout=0, filter_res_func=None):
        func_name = func.__name__ if hasattr(func, '__name__') else repr(func),
        start_time = time.time()
        all_num = 0
        filter_res_num = 0

        logger_info('[开始] 消费 [{}()] {}'.format(func_name, its.__class__))
        for index, it in enumerate(cls.show_process(its)):
            res = func(it)
            time_use = time.time() - start_time
            if index < log_size or (not index % log_re):
                logger_info('[{:.1f}s] 消费 第 [{:08d}] 次执行 [{}({})] 将返回 {}'.format(
                    time_use, index + 1, func_name, repr(it), repr(res)[:50]))
            if filter_res_func and filter_res_func(res):
                filter_res_num += 1
            else:
                yield res
            all_num = index + 1
            if timeout and time_use > timeout:
                break

        logger_info('[{:.1f}s] 消费 一共执行 [{}()] [{:08d}] 次,其中 [{:08d}] 次结果被过滤'.format(
            time.time() - start_time, func_name, all_num, filter_res_num))

    @classmethod
    def for_do_list(cls, func, its, log_size=1, log_re=1000, timeout=0, filter_res_func=None):
        func_name = func.__name__ if hasattr(func, '__name__') else repr(func),
        start_time = time.time()
        results = []
        all_num = 0
        filter_res_num = 0
        logger_info('[开始] 消费 [{}()] {}'.format(func_name, its.__class__))
        for index, it in enumerate(cls.show_process(its)):
            res = func(it)
            time_use = time.time() - start_time
            if index < log_size or (not index % log_re):
                logger_info('[{:.1f}s] 消费 第 [{:08d}] 次执行 [{}({})] 将返回 {}'.format(
                    time_use, index + 1, func_name, repr(it), repr(res)[:50]))
            if filter_res_func and filter_res_func(res):
                filter_res_num += 1
            else:
                results.append(res)
            all_num = index + 1
            if timeout and time_use > timeout:
                break

        logger_info('[{:.1f}s] 消费 一共执行 [{}()] [{:08d}] 次,其中 [{:08d}] 次结果被过滤'.format(
            time.time() - start_time, func_name, all_num, filter_res_num))
        return results


def active_log():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger.setLevel(logging.INFO)


if __name__ == '__main__':
    tmp_logger_debug = functools.partial(print, '[DEBUG]')
    logger_debug = lambda x: tmp_logger_debug(repr(x))
    Dao(range, print)(1, 10)

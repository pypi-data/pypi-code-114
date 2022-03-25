# @Time : 2022/3/9 3:54 PM 
# @Author : SailYang
import re


class TestFilter:
    def __init__(self, test_suites):
        # test_suites 为测试用例列表集合
        self.suites = test_suites

        # 添加一个被忽略的测试用例集合
        self.exclude_suites = None

    # 标签筛选策略，只要包括即运行
    def filter_tags_in_any(self, user_option_tags):
        included_cls = []
        remain_cases = []

        # 将被忽略的测视用例添加到 excluded_cases 列表
        excluded_cases = []

        for i in self.suites:
            # 找到每个测试用例的tag
            tags_in_class = i[0]
            tags = []

            # 命令行输入的tag 有可能是个列表集合，需要递归找出来
            def recursion(raw_tag):
                if raw_tag:
                    if isinstance(raw_tag, (list, tuple)):
                        for item in raw_tag:
                            if isinstance(item, (list, tuple)):
                                recursion(item)
                            else:
                                tags.append(item)
                    else:
                        # 如果只有一个tag，传化成['tag']形式
                        return re.split(r'[;,\s]\s*', raw_tag)
                return tags

            after_parse = recursion(tags_in_class)

            """
            lambda x: True if x in after_parse else False 
            可以分解为:
            if x in after_parse:
                lambda x:True
            else:
                False
            通过map方法，将user_option_tags也就是tag列表集合中每个tag分别带入到 x 中，如果x在after_parse中就返回True，反之为False。
            得到列表类似于 [False,True,False,...]，any方法为入参只要有一个为True，就返回True
            """
            # 判断命令行输入的tag是否匹配上测试用例tag集合
            if any(map(lambda x: True if x in after_parse else False, user_option_tags)):
                included_cls.append(i[0])

        # 找到命令行输入的tag装饰的测试用例，如果没有 tag 装饰的测试利用将被添加进 excluded_cases
        for s in self.suites:
            if s[0] in set(included_cls):
                remain_cases.append(s)
            else:
                excluded_cases.append(s)
        self.suites = remain_cases
        self.exclude_suites = excluded_cases

    # 返回tag装饰的测试用例
    def tag_filter_run(self, in_any_tags):
        if in_any_tags:
            self.filter_tags_in_any(in_any_tags)

        # 同时返回带测试的用例集和被忽略的测试集
        return self.suites, self.exclude_suites

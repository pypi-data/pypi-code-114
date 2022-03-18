import os
import requests
import pandas as pd


class Taos:
    def __init__(self, host, db, user, password, port=6041):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.port = port
        self.url = "http://%s:%s/rest/sql/%s" % (self.host, self.port, self.db)

    def restful_execute(
            self,
            sql: str,
            not_succ_raise: bool = False,
    ) -> dict:
        """
        用 restful 方式执行 sql 命令到 taos 数据库
        :param sql: sql 语句
        :param not_succ_raise: 状态不为 succ 的时候, 是否抛出异常
        :return:
        """
        resp = requests.post(
            self.url,
            sql.encode('utf-8'),
            auth=(self.user, self.password)
        )
        result_dict = resp.json()
        if result_dict['status'] != 'succ':
            result_dict['cmd'] = sql
            msg = str(result_dict)
            if not_succ_raise:
                raise Exception(msg)
        return result_dict

    def get_values_tags_headers(self, stable: str) -> dict:
        """
        获取一个超级表的 headers, 分开 values 和 tags
        return: dict
        """
        d = {
            "values": [],
            "tags": []
        }
        sql = f"describe {self.db}.`{stable}`"
        result_dict = self.restful_execute(sql)
        data_list = result_dict['data']
        for data in data_list:
            if data[-1] == "TAG":
                d['tags'].append(data[0])
            else:
                d['values'].append(data[0])
        return d

    def to_dataframe(self, sql: str, stable: str = None,
                     not_succ_raise: bool = False,
                     values_or_tags: str = 'both') -> pd.DataFrame:
        """

        :param sql: sql 语句
        :param stable: 超级表
        :param values_or_tags: {"both", "values", "tags"}
            both: 全部
            values: 只筛选 values 的列
            tags: 只筛选 tags 的列
        :param not_succ_raise: 状态不为 succ 的时候, 是否抛出异常
        :return: pd.DataFrame
        """
        result_dict = self.restful_execute(sql, not_succ_raise=not_succ_raise)
        df = pd.DataFrame(data=result_dict['data'], columns=result_dict['head'])

        if values_or_tags == "both":
            return df
        elif values_or_tags == "values":
            # 是值的列名
            value_headers = self.get_values_tags_headers(stable=stable)['values']
            return df[value_headers]
        elif values_or_tags == "tags":
            tags_headers = self.get_values_tags_headers(stable=stable)['tags']
            return df[tags_headers]
        else:
            raise Exception("传入 values_or_tags 参数有误, 请传入 values, tags, both 中的一个")

    def check_columns_if_match(self, map_path: str):
        """检查被读的字典表与已经存在的 taos 数据库是否匹配, 检查列名与顺序"""
        # 1. 获取超级表名称
        stable = os.path.basename(map_path).split("_")[0]

        sql = f"describe `{stable}`;"

        result_dict = self.restful_execute(sql)

        if result_dict['status'] == 'error' and result_dict['desc'] == 'Table does not exist':
            print(f'检查OK: 还不存在 {stable}')
            return
        df_taos = pd.DataFrame(data=result_dict['data'], columns=result_dict['head'])

        # 1. 检查 values
        df_map = pd.read_csv(map_path, usecols=['子域', '字段类型'])
        assert str(df_map.loc[0, '子域']).lower() == 'ts', f"{map_path} 子域的第一个值必须是 ts 或 Ts, 而不是 {df_map.loc[0, '子域']}"
        df_map.loc[0, '子域'] = 'ts'
        df_taos_values_cols = df_taos[df_taos['Note'] == '']['Field'].values.tolist()
        df_map_values_cols = df_map[df_map["字段类型"].isin(['ts', 'Ts', 'value'])]['子域'].values.tolist()
        assert df_taos_values_cols == df_map_values_cols, f"字典表 {map_path} 与 数据库超级表 {stable} 的 values 不匹配, df_map: {df_map_values_cols}, df_taos: {df_taos_values_cols}"

        # 2. 检查 columns
        df_taos_columns_cols = df_taos[df_taos['Note'] == 'TAG']['Field'].values.tolist()
        df_map_columns_cols = df_map[df_map["字段类型"] == 'tag']['子域'].values.tolist()
        df_map_columns_cols = ['uuid', 'name', 'display_name', 'user_name'] + df_map_columns_cols
        assert df_taos_columns_cols == df_map_columns_cols, f"字典表 {map_path} 与 数据库超级表 {stable} 的 tag 不匹配, df_map: {df_map_columns_cols}, df_taos: {df_taos_columns_cols}"
        print(f"检查OK: {map_path}")

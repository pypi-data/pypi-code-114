# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:00
# Copyright (c) 2022
# author: Euraxluo


import random
import asyncio
from concurrent import futures
from amap_distance_matrix.helper import *
from amap_distance_matrix.schemas.amap import *
from amap_distance_matrix.services.register import register

"""
高德地图webapi接口服务包装
"""


###############navigating################

def navigating_url(origin: list, destination: list, waypoints: list = None,
                   batch_size: int = 12, strategy: int = 1, output: str = "json",
                   key: str = None, host: str = "https://restapi.amap.com/v3/direction/driving") -> list:
    """
    将waypoints包装为driving_url urls
    :param host:
    :param origin:
    :param destination:
    :param batch_size:
    :param strategy:
    :param output:
    :param key:
    :param waypoints:
    :return:
    """
    if waypoints is None:
        waypoints = []
    if key is None and register.keys:
        key = register.keys
    if isinstance(key, list):
        key = random.choice(key)
    urls = []
    paths = [origin] + waypoints + [destination]
    if not waypoints:
        urls.append(f"{host}?strategy={strategy}&origin={loc_to_str([origin])}&destination={loc_to_str([destination])}&output={output}&key={key}")
        return urls
    for idx in [(i, i + batch_size) for i in range(0, len(paths), batch_size)]:
        tmp_points = paths[idx[0] - 1 if idx[0] > 1 else 0:idx[1]]
        if len(tmp_points) <= 2:
            urls.append(f"{host}?strategy={strategy}&origin={loc_to_str([tmp_points[0]])}&destination={loc_to_str([tmp_points[-1]])}&output={output}&key={key}")
        else:
            urls.append(
                f"{host}?strategy={strategy}&origin={loc_to_str([tmp_points[0]])}&destination={loc_to_str([tmp_points[-1]])}&waypoints={loc_to_str(tmp_points[1:-1])}&output={output}&key={key}")
    return urls


def request_navigating(url, idx, data_list):
    """
    通过导航url获取导航数据并进行结果设置
    :param url: 导航url
    :param idx: 结果集合索引
    :param data_list:
    :return:
    """
    try:
        data = register.session().get(url).json()
        if data['infocode'] == '10000':
            data_list[idx] = data
        else:
            raise Exception(data['infocode'])
    except Exception as e:
        register.logger.warning(f"Autonavi Error:{e},url:{url}")


def default_data_with_navigating_url(url, idx, data_list):
    points = []
    end_point = None
    for token in url.split('&'):
        if token.startswith("origin"):
            points.append(token.split('=')[-1])
        elif token.startswith("destination"):
            end_point = token.split('=')[-1]
        elif token.startswith("waypoints"):
            points.extend(token.split('=')[-1].split(';'))
    points.append(end_point)
    data_list[idx] = AMapDefaultResult(points=points).__dict__
    return data_list[idx]


def futures_navigating(urls: list) -> dict:
    """
    异步 基于 drive url list 通过请求高德接口 获得 路径规划结果
    :param urls:
    :return:
    """
    data_collections = [None] * len(urls)
    pack_data_result = {}
    all_tasks = []
    # 准备
    try:
        event_loop = asyncio.get_event_loop()
    except RuntimeError as _:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        event_loop = asyncio.get_event_loop()
    executors = futures.ThreadPoolExecutor((len(urls) // 10 + 1))
    # 添加task
    for idx in range(len(urls)):
        all_tasks.append(event_loop.run_in_executor(executors, request_navigating, urls[idx], idx, data_collections))
    # 运行
    event_loop.run_until_complete(asyncio.wait(all_tasks))
    # 获取结果,只获取 ['route']['paths'][0] ,也即只获取第一种策略的数据
    for idx in range(len(urls)):
        api_data_result = data_collections[idx]
        if not api_data_result:
            # 再尝试换一个key获取一下
            all_token = urls[idx].split('&')
            key_idx = -1
            for i, token in enumerate(all_token):
                if token.startswith("key"):
                    old_key = token.split('=')[-1]  # TODO:旧的key,可以降低权重等
                    key_idx = i
            if key_idx > 0:
                all_token[key_idx] = f"key={random.choice(register.keys)}"
            urls[idx] = "&".join(all_token)
            request_navigating(urls[idx], idx, data_collections)
            if not data_collections[idx]:
                api_data_result = default_data_with_navigating_url(urls[idx], idx, data_collections)
        if not pack_data_result:
            pack_data_result = api_data_result
            pack_data_result['route']['paths'] = [pack_data_result['route']['paths'][0]]
        else:
            pack_data_result['route']['destination'] = api_data_result['route']['destination']

            pack_data_result['route']['taxi_cost'] = str(
                float(pack_data_result['route']['taxi_cost']) + float(api_data_result['route']['taxi_cost']))

            pack_data_result['route']['paths'][0]['distance'] = str(
                float(pack_data_result['route']['paths'][0]['distance']) + float(api_data_result['route']['paths'][0]['distance']))

            pack_data_result['route']['paths'][0]['duration'] = str(
                float(pack_data_result['route']['paths'][0]['duration']) + float(api_data_result['route']['paths'][0]['duration']))

            pack_data_result['route']['paths'][0]['tolls'] = str(
                float(pack_data_result['route']['paths'][0]['tolls']) + float(api_data_result['route']['paths'][0]['tolls']))

            pack_data_result['route']['paths'][0]['toll_distance'] = str(
                float(pack_data_result['route']['paths'][0]['toll_distance']) + float(
                    api_data_result['route']['paths'][0]['toll_distance']))

            pack_data_result['route']['paths'][0]['steps'].extend(api_data_result['route']['paths'][0]['steps'])

    return pack_data_result


def futures_driving(origin: list, destination: list, waypoints: list = None, strategy=5, output="json", key: str = None,
                    host: str = "https://restapi.amap.com/v3/direction/driving", batch_size: int = 12) -> dict:
    """
    异步进行导航url的构建,以及请求
    :param origin: [float,float]
    :param destination: [float,float]
    :param waypoints :[[float,float],[float,float],[float,float]]
    :param strategy: int 1-10
    :param output: str "json"
    :param key: str amap_web_api_key  "6828ea8c1670e149413299d8216c13ee"
    :param host: str host_name "https://restapi.amap.com/v3/direction/driving"
    :param batch_size: 每个url的batch
    :return:
    """
    if waypoints is None:
        waypoints = []
    if key is None and register.keys:
        key = random.choice(register.keys)
    urls = navigating_url(host=host, origin=origin, destination=destination,
                          batch_size=batch_size,
                          strategy=strategy, waypoints=waypoints, output=output, key=key)
    return futures_navigating(urls=urls)


def driving_batch(origin: list, destination: list, waypoints: list = None, check_points: tuple = ("到达途经地", "到达目的地"),
                  road_status_calculate: tuple = (0.5, ("畅通", "未知")), autonavi_config: dict = None):
    """
    批量异步的进行路径规划,并返回路径规划的结果
    :param origin:起始点 \n
    :param destination:终点 \n
    :param waypoints:途经点 \n
    :param check_points:检查点列表 tuple(检查点标识) \n
    :param road_status_calculate:路况 tuple(畅通路段系数,tuple(畅通路段标识))  计算公式:+(road_status_calculate[0])*road_distance if road_statu in road_status_calculate[1] else -(1-road_status_calculate[0])*road_distance \n
    :param autonavi_config: autonavi_config字典
        {
             strategy: int 1-10 \n
             output: str "json" \n
             key: str amap_web_api_key  "6828ea8c1670e149413299d8216c13ee" \n
             host: str host_name "https://restapi.amap.com/v3/direction/driving"
        }
    :return:[{'origin':[float,float],'destination':[float,float],'strategy':str,'total_duration':int,'total_distance':int,'assistant_action':int,'tmcs':float,'step':[{'distance':int,'duration':int,'polyline':str('float,float;float,float'}]}]
    """
    if waypoints is None:
        waypoints = []
    if autonavi_config is None:
        autonavi_config = {}
    data = futures_driving(origin=origin, destination=destination, waypoints=waypoints, **autonavi_config)
    if data['status'] != '1':
        return None
    route = data['route']
    origin_loc = format_loc(route['origin'])
    destination_loc = format_loc(route['destination'])
    route_path = route['paths'][0]
    waypoints_planning = {
        "origin": origin_loc,
        "destination": destination_loc,
        "strategy": route_path['strategy'],
        "total_duration": float(route_path['duration']),
        "total_distance": float(route_path['distance']),
        "steps": []
    }
    check_point = 1  # 检查点初始值
    total_waypoints = [origin] + waypoints + [destination]
    waypoints_step = list(zip(total_waypoints, total_waypoints[1:]))
    for idx, step in enumerate(route_path['steps']):
        road_status = sum([road_status_calculate[0] * float(tmc['distance'])
                           if tmc['status'] in road_status_calculate[1]
                           else -(1 - road_status_calculate[0]) * float(tmc['distance']) for tmc in
                           step['tmcs']])
        cur_check_point = 1 if step['assistant_action'] in check_points else 0  # 当前检查点值
        # 计算是否需要add/append,公式: old_check_point * (old_check_point or cur_check_point) = old_check_point
        if check_point * (check_point or cur_check_point) == 0:
            tmp_tmcs = waypoints_planning['steps'][-1]
            tmp_tmcs['polyline'] += ";" + step['polyline']
            tmp_tmcs['tmc'] += road_status
            tmp_tmcs['distance'] += float(step['distance'])
            tmp_tmcs['duration'] += float(step['duration'])
        else:
            step_tmcs = {
                "distance": float(step['distance']),
                "duration": float(step['duration']),
                "polyline": step['polyline'],
                "tmc": road_status,
                "origin": waypoints_step[len(waypoints_planning['steps'])][0],
                "destination": waypoints_step[len(waypoints_planning['steps'])][1],
            }
            waypoints_planning['steps'].append(step_tmcs)

        check_point = cur_check_point

    return waypoints_planning

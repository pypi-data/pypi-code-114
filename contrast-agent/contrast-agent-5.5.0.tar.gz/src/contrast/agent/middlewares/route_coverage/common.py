# -*- coding: utf-8 -*-
# Copyright © 2022 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
from contrast.api import Route
from contrast.agent.middlewares.route_coverage.coverage_utils import (
    CoverageUtils,
    DEFAULT_ROUTE_METHODS,
)


def create_routes(app):
    """
    Returns all the routes registered to an app as a dict
    :param app: {Quart or Flask} app
    :return: dict {route_id:  api.Route}
    """
    routes = {}

    for rule in list(app.url_map.iter_rules()):
        view_func = app.view_functions[rule.endpoint]

        route = build_route(rule.endpoint, view_func)

        route_id = str(id(view_func))

        methods = rule.methods or DEFAULT_ROUTE_METHODS

        for method_type in methods:
            key = CoverageUtils.build_key(route_id, method_type)
            routes[key] = Route(
                verb=method_type,
                url=CoverageUtils.get_normalized_uri(str(rule)),
                route=route,
            )

    return routes


def build_route(view_func_name, view_func):
    view_func_args = CoverageUtils.build_args_from_function(view_func)
    return view_func_name + view_func_args


def get_view_func_for_request(request, app):
    """
    Find the view function for the current request in the app.
    :param request: current request
    :param app: {Quart or Flask} app
    :return: function
    """
    from werkzeug.exceptions import NotFound

    adapter = app.url_map.bind("empty")

    if None in (request, adapter):
        return None

    try:
        match = adapter.match(request.path, method=request.method)
    except NotFound:
        match = None

    func = None
    if match is not None:
        func = app.view_functions[match[0]]

    return func

#!/usr/bin/env python

"""Tests for `threaded_mvc` package."""

import pytest

import threaded_mvc.model, threaded_mvc.view, threaded_mvc.controller

def test_model_class_is_abstract():
    with pytest.raises(TypeError):
        mvcmodel = threaded_mvc.model.Model()

def test_view_class_is_abstract():
    with pytest.raises(TypeError):
        mvcview = threaded_mvc.view.View()

def test_controller_class_is_abstract():
    with pytest.raises(TypeError):
        mvccontroller = threaded_mvc.controller.Controller()

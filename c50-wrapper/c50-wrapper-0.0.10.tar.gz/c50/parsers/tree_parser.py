# -*- coding: utf-8 -*-
"""
Module tree_parser.py
------------------------
A parser for the decision tree text output;
C5.0 is a opensource decision tree algorithm written in `c` programming language.
For more information please refer to their (official website)[https://www.rulequest.com/see5-unix.html#USE].   
"""
import pyparsing as pp
from .base_parser import BaseParser
from .parser_types import StringType, IntType, FloatType, SetType


class FeatureName(BaseParser):

    def __init__(self, features):
        self.features = features
        super(FeatureName, self).__init__()

    def __init_elem__(self):
        return (
            pp.one_of(
                list(self.features),
                caseless=True
            )
        ).set_results_name("feature_name")
    

class ComparisonOperator(BaseParser):
    __parse_element__ = (
        pp.one_of(
            ['>', '<', '<=', '>=', '=', 'in', '<>', '!='],
            caseless=True
        ).set_results_name('comparison_operator')
    )

    def parse_action(self, tokens:pp.ParseResults):
        t = tokens[0]

        if t[0] == '<>':
            t[0] = '!='
            t['comparison_operator'] = '!='

        elif t[0] == '=':
            t[0] = '=='
            t['comparison_operator'] = "=="


class NodeLevelMarks(BaseParser):
    __parse_element__ = pp.ZeroOrMore(
        pp.Literal('|')
    ).set_results_name('node_level_marks')


class Prediction(BaseParser):
    
    def __init__(self, labels):
        self.labels = labels
        super(Prediction, self).__init__()

    def __init_elem__(self):
        nm = pp.Or(
            [
                IntType(),
                FloatType(),
            ]
        )
        
        return (
            pp.one_of(self.labels, caseless=True) + 
            pp.Literal('(').suppress() + nm + pp.Opt('/' + nm) + pp.Literal(')').suppress()
        ).set_results_name('prediction')


    def parse_action(self, tokens:pp.ParseResults):
        t = tokens[0]
        t['label'] = t[0]
        t['n'] = t[1]
        if len(t) > 2:
            t['m'] = t[2]
        else:
            t['m'] = None

class TreeNode(BaseParser):

    def __init__(self, features, labels):
        self.features = features
        self.labels = labels
        super(TreeNode, self).__init__()

    def __init_elem__(self):
        value = pp.Or(
            [
                IntType(),
                FloatType(),
                StringType(),
                SetType()
            ]
        )
        return (
            NodeLevelMarks() + 
            FeatureName(self.features) + 
            ComparisonOperator() +
            value + pp.Literal(":").suppress() +
            pp.Opt(
                Prediction(self.labels)
            )
        )
    
    def parse_action(self, tokens:pp.ParseResults):
        t = tokens[0]
        # number of '|' (level marks)
        t['node_level'] = len(t[0].node_level_marks)
        t['feature_name'] = t[1].feature_name
        t['operator'] = t[2].comparison_operator
        t['value'] = t[3].value
        # if node has a prediction element
        if len(t) == 5:
            t['is_terminal'] = True
            t['label'] = t[4].label
        else:
            t['is_terminal'] = False
            t['label'] = None


class Tree(BaseParser):

    def __init__(self, features, labels):
        self.features = features
        self.labels = labels
        self.rules = list()
        self.r_labels = list()
        super(Tree, self).__init__()

    def __init_elem__(self):
        return pp.OneOrMore(
            TreeNode(self.features, self.labels)
        ).set_results_name('nodes')
    
    def parse_action(self, tokens: pp.ParseResults):
        t = tokens[0]

    def parse_rules(self, nodes):
        current = -1
        while current < (len(nodes) -1):
            current = self._parse_rules(nodes, current + 1, '')
        
        return self.rules, self.r_labels

    def _parse_rules(self, nodes, current, rule):
        # if current > 0 and nodes[current].node_level <=
        if len(rule) > 0:
            rule += f" & `{nodes[current].feature_name}` {nodes[current].operator} {nodes[current].value}"
        else:
            rule += f"`{nodes[current].feature_name}` {nodes[current].operator} {nodes[current].value}"
        
        if nodes[current].is_terminal:
            self.rules.append(rule)
            self.r_labels.append(nodes[current].label)
            return current
        
        new_current = current
        while nodes[new_current + 1].node_level > nodes[current].node_level:
            new_current = self._parse_rules(nodes, new_current+1, rule)

            if new_current == (len(nodes) - 1):
                return new_current
        
        return new_current

        
        
        
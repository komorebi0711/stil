# -*- coding: utf-8 -*-
import inspect


class TimingBlockParser:
    def __init__(self, debug=True):
        self.debug = debug

    def trace(self, func_name, t):
        head = f"{__name__}:{func_name}"

        if isinstance(t, list):
            print(f"{head} rule value {t}")
        else:
            print(f'{head} token value "{t}" at line {t.line} column {t.column}')

    def b_timing__TIMING_DOMAIN_NAME(self, t):
        if self.debug:
            func_name = inspect.stack()[0][3]
            self.trace(func_name, t)

    def b_timing__OPEN_TIMING_BLOCK(self, t):
        if self.debug:
            func_name = inspect.stack()[0][3]
            self.trace(func_name, t)

    def b_timing__CLOSE_TIMING_BLOCK(self, t):
        if self.debug:
            func_name = inspect.stack()[0][3]
            self.trace(func_name, t)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:      dudea
# @Time:        2022/5/18 11:15
import json
import logging
import sys
import time
import traceback


class JsonFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)

    default_msec_format = '%s.%03d'

    # def converter(self, timestamp):
    #     return time.gmtime(timestamp)

    def format(self, record):
        formatted_record = dict(
            deal_time=self.formatTime(record),
            level=getattr(record, "levelname"),
            app_type=getattr(record, "name"),
            business_type=getattr(record, "business_type"),
            source=getattr(record, "source"),
            trace_id=getattr(record, "trace_id"),
            deal_stage=getattr(record, "deal_stage"),
            object_uuid=getattr(record, "object_uuid"),
            spend=getattr(record, "spend"),
            message=getattr(record, "msg")
        )

        return json.dumps(formatted_record, ensure_ascii=False)

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            s = time.strftime(self.default_time_format, ct)
        s = self.default_msec_format % (s, record.msecs)
        return s


def setlogrootname(name):
    logger.name = name


def setloglevel(key):
    if key.lower() == "debug":
        logger.setLevel(logging.DEBUG)
    elif key.lower() == "info":
        logger.setLevel(logging.INFO)
    elif key.lower() == "warning":
        logger.setLevel(logging.WARNING)
    elif key.lower() == "exception":
        logger.setLevel(logging.ERROR)
    elif key.lower() == "error":
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.INFO)


logger = logging.getLogger("pz_core_fastapi")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.formatter = JsonFormatter()
logger.addHandler(handler)


def __extra_check(**kwargs):
    if 'extra' not in kwargs:
        kwargs['extra'] = {}
        kwargs['extra']['business_type'] = kwargs['extra'].get("business_type")
        kwargs['extra']['deal_stage'] = kwargs['extra'].get("deal_stage")
        kwargs['extra']['object_uuid'] = kwargs['extra'].get("object_uuid")
        kwargs['extra']['source'] = kwargs['extra'].get("source")
        kwargs['extra']['trace_id'] = kwargs['extra'].get("trace_id")
        kwargs['extra']['spend'] = kwargs['extra'].get("spend")
    return kwargs


def info(msg, *args, **kwargs):
    if type(msg) != str:
        msg = msg.__str__()
    kwargs = __extra_check(**kwargs)
    logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    if type(msg) != str:
        msg = msg.__str__()
    kwargs = __extra_check(**kwargs)
    logger.warning(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    if type(msg) != str:
        msg = msg.__str__()
    kwargs = __extra_check(**kwargs)
    logger.debug(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    kwargs['exc_info'] = False
    exc_type, exc_value, exc_traceback = sys.exc_info()
    errmsg = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
    msg = msg + errmsg
    msg = msg.replace("\"", "'")
    kwargs = __extra_check(**kwargs)
    logger.error(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    errmsg = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
    msg = msg + errmsg
    msg = msg.replace("\"", "'")
    kwargs = __extra_check(**kwargs)
    logger.error(msg, *args, **kwargs)

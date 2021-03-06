# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: apis.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 12月 29, 2020
# ---------------------------------------------
from flask_restful import Resource
from libs.status import s
from libs.result import bulid_success, bulid_fail
from libs.decorators import login_wrapper
from libs.emuns import Codes
from flask import current_app, request, session
from apps.services.login_service import check_pwd


class Hello(Resource):
    """hello"""

    @login_wrapper
    def get(self):
        current_app.logger.info('Hello World!')
        return bulid_success(result={"hello status:": s.status})


class Heart(Resource):
    """心跳"""

    @login_wrapper
    def post(self):
        current_app.logger.info('rev heart:{}'.format(request.get_json()))
        return bulid_success()


class Login(Resource):
    """
        登录
        {"username":"abc","password":"123"}
    """

    def post(self):
        r = request.get_json()
        if not r or not r.get("username"):
            return bulid_fail()
        user = r.get("username")
        pwd = r.get("password")
        if check_pwd(user, pwd):
            session["username"] = user
            return bulid_success()
        else:
            return bulid_fail(Codes.USER_PAW_ERROR)

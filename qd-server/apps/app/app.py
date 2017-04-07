#-*- coding:utf-8 -*-

import turbo.log

from base import BaseHandler
from helpers import qiandao

qd = qiandao.qian_dao
logger = turbo.log.getLogger(__file__)


class HomeHandler(BaseHandler):

    def get(self):
        self.render('index.html')


class QiandaoHandler(BaseHandler):
    def get(self):
        mobile = self.get_argument('mobile', None)
        op = self.get_argument('op', None)

        if op == 'on':
            qd.on(mobile)
        elif op == 'off':
            qd.off(mobile)
        else:
            rs = qd.find_qiandao(mobile)
            if rs.get('error'):
                self.render('index.html', msg=rs)
            else:
                self.render('qiandao.html', qiandao=rs)


class AdminHandler(BaseHandler):
    def get(self):
        self.render('admin.html', list=qd.find_all_auto())
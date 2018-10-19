# -*- coding: utf-8 -*
import sqlite3,json
from util.constant import Constant
class BasicDao(object):

    TASK_INFO_BY_USER_ID = r'select id,name,url,theme,category,acq_type,rule,user,state from rb_task where id = ?'
    TASK_INFO_BY_CATEGORY = r'select id,name,url,theme,category,acq_type,rule,user,state from rb_task where category = ?'
    QUERY_THEMES = r'select id,name,code from rb_theme'
    QUERY_CATETORY_BY_THEME = r'select id,name,code,parent from rb_category where theme = ?'
    QUERY_CATEGORY_BY_PARENT = r'select id,name,code,parent from rb_category where parent = ?'
    INSERT_SINGLE_TASK = r'insert into rb_task values (null,?,?,?,?,?,?,?,?)'
    UPDATE_SINGLE_TASK = r'update rb_task set name = ?, url = ?, theme = ?, category = ?,acq_type = ? ,rule = ? where id = {}'
    DELETE_TASK_BY_IDS = r'delete from rb_task where id in ({})'
    DELETE_ACQ_STRATEGY_BY_IDS = r'delete from rb_acq_strategy where task_id in ({})'
    QUERY_ACQ_RULE_BY_TASK_ID = r'select id,rule from rb_acq_strategy where task_id = ?'
    UPDATE_ACQ_RULE_BY_TASK_ID = r'update rb_acq_strategy set rule = ? where task_id = ?'
    INSERT_ACQ_RULE = r'insert into rb_acq_strategy values (null,?,?)'


    @classmethod
    def task_info_by_id(cls,id):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            info = {}
            rows = c.execute(BasicDao.TASK_INFO_BY_USER_ID,(id,))
            for row in rows:
                info['id'] = row[0]
                info['name'] = row[1]
                info['url'] = row[2]
                info['theme'] = row[3]
                info['category'] = row[4]
                info['acqType'] = row[5]
                info['rule'] = row[6]
                info['user'] = row[7]
                info['state'] = row[8]

            return info
        except Exception as a:
            return None
        finally:
            conn.commit()
            conn.close()

    @classmethod
    def task_info_by_category(cls,code):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            list = []
            rows = c.execute(BasicDao.TASK_INFO_BY_CATEGORY,(code,))
            for row in rows:
                info = {}
                info['id'] = row[0]
                info['name'] = row[1]
                info['url'] = row[2]
                info['theme'] = row[3]
                info['category'] = row[4]
                info['acqType'] = row[5]
                info['rule'] = row[6]
                info['user'] = row[7]
                info['state'] = row[8]
                list.append(info)

            return list
        except Exception as a:
            return None
        finally:
            conn.commit()
            conn.close()


    @classmethod
    def get_all_theme(cls):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            rows = c.execute(BasicDao.QUERY_THEMES)
            list = []
            for row in rows:
                info = {}
                info['id'] = row[0]
                info['name'] = row[1]
                info['code'] = row[2]
                list.append(info)
            return list
        except Exception as a:
            return []
        finally:
            conn.commit()
            conn.close()

    @classmethod
    def get_category_by_theme(cls,theme_code,flag):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            if flag:
                rows = c.execute(BasicDao.QUERY_CATETORY_BY_THEME,(theme_code,))
            else:
                rows = c.execute(BasicDao.QUERY_CATETORY_BY_THEME+" and parent = 0",(theme_code,))
            list = []
            for row in rows:
                info = {}
                info['id'] = row[0]
                info['name'] = row[1]
                info['code'] = row[2]
                info['parent'] = row[3]
                list.append(info)
            return list
        except Exception as a:
            return []
        finally:
            conn.commit()
            conn.close()


    @classmethod
    def get_category_by_parent(cls,parent):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            rows = c.execute(BasicDao.QUERY_CATEGORY_BY_PARENT,(parent,))
            list = []
            for row in rows:
                info = {}
                info['id'] = row[0]
                info['name'] = row[1]
                info['code'] = row[2]
                info['parent'] = row[3]
                list.append(info)
            return list
        except Exception as a:
            return []
        finally:
            conn.commit()
            conn.close()



    @classmethod
    def insert_single_task(cls,content):
        """
        插入单条任务，返回主键id
        :param content:
        :return:
        """
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            result = c.execute(BasicDao.INSERT_SINGLE_TASK,(content['basic']['name'],content['basic']['url'],
                                                content['basic']['theme'],content['basic']['category'],
                                                content['basic']['acqType'],json.dumps(content['rule']),
                                                content['basic']['user'],content['basic']['state']))
            return result.lastrowid
        except Exception as a:
            print(a)
            return None
        finally:
            conn.commit()
            conn.close()


    @classmethod
    def update_single_task(cls,content):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            c.execute(BasicDao.UPDATE_SINGLE_TASK.format(content['basic']['id']),(content['basic']['name'],content['basic']['url'],
                                                   content['basic']['theme'],content['basic']['category'],content['basic']['acqType'],
                                                   json.dumps(content['rule'])))
        except Exception as a:
            print(a)
            return []
        finally:
            conn.commit()
            conn.close()


    @classmethod
    def delete_task_by_ids(cls,ids):
        """
        根据id删除站点任务,同时删除关联的采集策略
        :param ids:
        :return:
        """
        try:
            idstr = ",".join(ids)
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            c.execute(BasicDao.DELETE_TASK_BY_IDS.format(idstr))
            c.execute(BasicDao.DELETE_ACQ_STRATEGY_BY_IDS.format(idstr))
            return True
        except Exception as a:
            return False
        finally:
            conn.commit()
            conn.close()

    @classmethod
    def query_strategy_by_taskid(cls,task_id):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            info = {}
            rows = c.execute(BasicDao.QUERY_ACQ_RULE_BY_TASK_ID,(task_id,))
            for row in rows:
                info['id'] = row[0]
                info['rule'] = row[1]
            return info
        except Exception as a:
            return None
        finally:
            conn.commit()
            conn.close()


    @classmethod
    def save_acq_strategy(cls,task_id,content):
        try:
            conn = sqlite3.connect(Constant.DB_PATH)
            c = conn.cursor()
            rule_list = c.execute(BasicDao.QUERY_ACQ_RULE_BY_TASK_ID,(task_id,))
            flag = []
            for rule in rule_list:
                flag.append(1)
            if flag:
                c.execute(BasicDao.UPDATE_ACQ_RULE_BY_TASK_ID,(content,task_id))
            else:
                c.execute(BasicDao.INSERT_ACQ_RULE,(task_id,content))
        except:
            pass
        finally:
            conn.commit()
            conn.close()
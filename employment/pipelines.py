# -*- coding: utf-8 -*-
import os
import logging
import pymongo


class PipelineMongodb(object):
    def open_spider(self, spider):
        try:
            self.client = pymongo.MongoClient(**spider.settings.get('MONGODB_CONFIG', {}))
            # user & password
            # mongo_user = spider.settings.get("MONGODB_USER")
            # mongo_pwd = spider.settings.get("MONGODB_PWD")
            # if mongo_user and mongo_pwd:
            #     db_auth = self.client.yapi
            #     db_auth.authenticate(mongo_user, mongo_pwd)
            # 集合名称
            col_name = os.environ.get('CRAWLAB_COLLECTION')
            self.collection = self.client[spider.settings.get('MONGODB_DB')][col_name]
        except Exception as e:
            logging.log(logging.ERROR, 'PipelineMongodb open_spider: ' + str(e))

    def process_item(self, item, spider):
        try:
            # 将 TaskID 赋值给 item
            item['task_id'] = os.environ.get('CRAWLAB_TASK_ID')
            self.collection.insert_one(dict(item))
        except Exception as e:
            logging.log(logging.ERROR, 'PipelineMongodb process_item: ' + str(e))
        return item

    def close_spider(self, spider):
        self.client.close()
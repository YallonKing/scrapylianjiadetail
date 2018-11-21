# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pymysql

from db.mysql_handle import MysqlHandler


class ScrapylianjiaPipeline(object):

    def open_spider(self,spider):
        self.mysql_handle = MysqlHandler(spider.settings['MYSQL_CONFIG'])


    def close_spider(self,spider):
        self.mysql_handle.dispose()

    # def process_item(self, item, spider):
    #     sql_params = [
    #         item['housecode'],
    #         item['title'],
    #         item['loc'],
    #         item['house_type'],
    #         item['area'],
    #         item['price'],
    #         item['follow'],
    #         item['watch'],
    #         item['unitPrice'],
    #         item['house_subinfo'],
    #         item['szlc'],
    #         item['hxjg'],
    #         item['tnmj'],
    #         item['jzlx'],
    #         item['fwcx'],
    #         item['jzjg'],
    #         item['zxqk'],
    #         item['thbl'],
    #         item['gnfs'],
    #         item['pbdt'],
    #         item['cqnx'],
    #         item['gpsj'],
    #         item['jyqs'],
    #         item['scjy'],
    #         item['fwyt'],
    #         item['fwnx'],
    #         item['cqss'],
    #         item['dyxx'],
    #         item['fbbj'],
    #         item['fybq'],
    #         item['zxms'],
    #         item['sfjx'],
    #         item['jtcx'],
    #         item['syrq'],
    #         item['hxmd']]
    #
    #     self.mysql_handle.insertOne('insert into lianjia(housecode,title,loc,house_type,area,price,follow,watch,unitPrice,house_subinfo,szlc,hxjg,tnmj,jzlx,fwcx,jzjg,zxqk,thbl,gnfs,pbdt,cqnx,gpsj,jyqs,scjy,fwyt,fwnx,cqss,dyxx,fbbj,fybq,zxms,sfjx,jtcx,syrq,hxmd) '
    #                                 'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', sql_params)
    #
    #     return item


from urllib.parse import quote
import pymysql.cursors
import scrapy
import re


class LianjiaSpider(scrapy.Spider):

    name = 'lianjia'

    start_urls = ['https://bj.lianjia.com/']

    def parse(self, response):
        keywords = self.settings['KEYWORDS']

        for keyword in keywords:
            url = f'https://bj.lianjia.com/ershoufang/rs{quote(keyword)}/'
            yield scrapy.Request(url,callback=self.parse_list,meta={'keyword':keyword})

    def parse_list(self,response):
            meta = response.meta
            keyword = meta['keyword']
            text = response.text
            totalPage = re.search(r'"totalPage":([0-9]+),',text).group(1)
            totalPage = int(totalPage)
            for i in range(1,totalPage+1):
                url = f'https://bj.lianjia.com/ershoufang/pg{i}rs{quote(keyword)}/'
                yield scrapy.Request(url, callback=self.parse_ershoufang, dont_filter=True, meta=meta)


    def parse_ershoufang(self,response):
        meta = response.meta
        url_detail = response.xpath('//div[@class="info clear"]/div[1]/a/@href').extract()
        for url in url_detail:
            yield scrapy.Request(url, callback=self.parse_ershoufang_detail, dont_filter=True, meta=meta)


    def parse_ershoufang_detail(self,response):
        housecode = ''.join(response.xpath('//div[@class="content"]/div[4]/div[4]/span[2]/text()').extract())
        title = ''.join(response.xpath('//div[@class="content"]/div[1]/h1/text()').extract())
        loc = ''.join(response.xpath('//div[@class="content"]/div[4]/div[1]/a[1]/text()').extract())
        house_type = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[1]/text()').extract())
        area = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[3]/text()').extract()).replace('㎡','')
        price = ''.join(response.xpath('//div[@class="price "]/span/text()').extract())
        follow = ''.join(response.xpath('//div[@class="action"]/span[@id="favCount"]/text()').extract())
        watch = ''.join(response.xpath('//div[@class="action "]/span[@id="cartCount"]/text()').extract())
        fwdj = ''.join(response.xpath('//div[@class="unitPrice"]/span/text()').extract())
        house_subinfo = ''.join(response.xpath('//div[@class="houseInfo"]/div[3]/div[2]/text()').extract())
        szlc = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[2]/text()').extract())
        hxjg = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[4]/text()').extract())
        tnmj = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[5]/text()').extract()).replace('㎡','')
        jzlx = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[6]/text()').extract())
        fwcx = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[7]/text()').extract())
        jzjg = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[8]/text()').extract())
        zxqk = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[9]/text()').extract())
        thbl = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[10]/text()').extract())
        gnfs = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[11]/text()').extract())
        pbdt = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[12]/text()').extract())
        cqnx = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li[13]/text()').extract()).replace('年','')
        gpsj = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[1]/span[2]/text()').extract())
        jyqs = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[2]/span[2]/text()').extract())
        scjy = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[3]/span[2]/text()').extract())
        fwyt = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[4]/span[2]/text()').extract())
        fwnx = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[5]/span[2]/text()').extract())
        cqss = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[6]/span[2]/text()').extract())
        dyxx = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[7]/span[2]/text()').extract()).replace(' ','').replace('\n','')
        fbbj = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li[8]/span[2]/text()').extract()).replace(' ','').replace('\n','')
        fybq = ''.join(response.xpath('//div[@class="introContent showbasemore"]/div[1]/div[2]/a/text()').extract()).replace(' ','').replace('\n','')
        zxms = ''.join(response.xpath('//div[@class="introContent showbasemore"]/div[2]/div[2]/text()').extract()).replace(' ','').replace('\n','')
        sfjx = ''.join(response.xpath('//div[@class="introContent showbasemore"]/div[3]/div[2]/text()').extract()).replace(' ','').replace('\n','')
        jtcx = ''.join(response.xpath('//div[@class="introContent showbasemore"]/div[4]/div[2]/text()').extract()).replace(' ','').replace('\n','')
        syrq = ''.join(response.xpath('//div[@class="introContent showbasemore"]/div[5]/div[2]/text()').extract()).replace(' ','').replace('\n','')
        hxmd = ''.join(response.xpath('//div[@class="introContent showbasemore"]/div[6]/div[2]/text()').extract()).replace(' ','').replace('\n','')
        url = ''.join(response.xpath('/html/head/link[2]/@href').extract())

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='lianjia', password='123456', db='lianjia',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        sql = "INSERT INTO lianjiadetail(housecode,title,loc,house_type,area,price,follow,watch,fwdj,house_subinfo,szlc,hxjg,tnmj,jzlx,fwcx,jzjg,zxqk,thbl,gnfs,pbdt,cqnx,gpsj,jyqs,scjy,fwyt,fwnx,cqss,dyxx,fbbj,fybq,zxms,sfjx,jtcx,syrq,hxmd,url) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(housecode,title,loc,house_type,area,price,follow,watch,fwdj,house_subinfo,szlc,hxjg,tnmj,jzlx,fwcx,jzjg,zxqk,thbl,gnfs,pbdt,cqnx,gpsj,jyqs,scjy,fwyt,fwnx,cqss,dyxx,fbbj,fybq,zxms,sfjx,jtcx,syrq,hxmd,url)
        cursor.execute(sql)
        connection.commit()

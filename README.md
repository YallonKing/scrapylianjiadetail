# scrapylianjiadetail
抓取链家网在售北京地区的二手房详细页面信息

mysql数据库表：
create table lianjiadetail1
(		housecode       varchar(500),
        title           varchar(500),
        loc             varchar(500),
        house_type      varchar(500),
        area            varchar(500),
        price           varchar(500),
        follow          varchar(500),
        watch		    varchar(500),
		unitPrice       varchar(500),
        house_subinfo   varchar(500),
        szlc            varchar(500),
        hxjg            varchar(500),
        tnmj            varchar(500),
        jzlx            varchar(500),
        fwcx            varchar(500),
        jzjg            varchar(500),
        zxqk            varchar(500),
        thbl            varchar(500),
        gnfs            varchar(500),
        pbdt            varchar(500),
        cqnx            varchar(500),
        gpsj            varchar(500),
        jyqs            varchar(500),
        scjy            varchar(500),
        fwyt            varchar(500),
        fwnx            varchar(500),
        cqss            varchar(500),
        dyxx            varchar(500),
        fbbj            varchar(500),
        fybq            varchar(500),
        zxms            varchar(500),
        sfjx            varchar(500),
        jtcx            varchar(500),
        syrq            varchar(500),
        hxmd            varchar(500)，
		url				varchar(500)
);

settings.py中设置抓取关键字信息
KEYWORDS = ['长丰园','天通苑','温泉花园']   #抓取指定关键字小区的房源信息
KEYWORDS = ['']                           #抓取北京地区所有房源信息

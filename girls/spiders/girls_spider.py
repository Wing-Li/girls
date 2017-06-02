import scrapy
from girls.items import GirlsItem


class GirlsSpider(scrapy.spiders.Spider):
    name = "girls"  # 唯一项目名
    allowed_domains = []  # 过滤域名
    start_urls = [
        "http://m.xxxiao.com/87188",  # 第一页地址
    ]

    def parse(self, response):
        item = GirlsItem()
        item['url'] = response.xpath("//*[@class='rgg-imagegrid gallery']//a//@href").extract()  # 提取图片链接
        yield item

        new_url = response.xpath('//div[@class="nav-links"]//a[@rel="next"]//@href').extract_first()  # 翻页
        if new_url:
            yield scrapy.Request(new_url, callback=self.parse)

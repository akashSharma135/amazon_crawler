from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AmazonScrpeItem
from amazon_scrpe.urls import url_list
import urllib

class AmazonCrawlSpider(CrawlSpider):
    name = 'amazon_crawl'
    allowed_domains = ['www.amazon.in']
    start_urls = url_list
    
    mobile_category_rule = Rule(LinkExtractor(restrict_css='ul > .a-spacing-micro a '), follow=True)
    mobile_detail_rule = Rule(LinkExtractor(restrict_css='.rush-component > a'), callback='parse_item', follow=False)
    next_page_rule = Rule(LinkExtractor(restrict_css='.a-last a'), follow=True)

    rules = (
        mobile_category_rule,
        mobile_detail_rule,
        next_page_rule
    )

    def parse_item(self, response):
        items = AmazonScrpeItem()
        url = response.url
        parsed_url = urllib.parse.urlparse(url)
        product_type = urllib.parse.parse_qs(parsed_url.query)['keywords']
        
        
        title = response.css('#productTitle::text').get().strip()
        image = response.css('#imgTagWrapperId > img::attr(src)').get()
        price = response.css('#priceblock_dealprice::text').extract() if response.css('#priceblock_dealprice::text') else response.css('#priceblock_ourprice::text').extract()
        
        lis = response.css('#feature-bullets > ul > li')
        data = []
        for li in lis:
            data.append(li.css('span::text').get().strip())
            
        
        items['title'] = title
        items['image'] = image
        items['type'] = product_type[0].replace('/', '')
        items['features'] = data
        items['price'] = price
        
       
        yield items
        
        
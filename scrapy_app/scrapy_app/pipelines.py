# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from main.models import News, Tweet


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        if item.get('type') == "news":
            news = News(
                headline=item.get('headline'),
                body=item.get('body'),
                url=item.get('url'),
                byline=item.get('byLine'),
                section=item.get('section'),
                picture=item.get('picture'),
            )
            news.save()
        elif item.get('type') == "tweet":
            tweet = Tweet(
                tweet=item.get('tweet'),
                time=item.get('time'),
                user=item.get('user'),
                user_name=item.get('user_name'),
                link=item.get('link'),
                user_picture=item.get('user_picture')
            )
            tweet.save()
        return item

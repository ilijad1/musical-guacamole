# -*- coding: utf-8 -*-
import json

import scrapy
from ..items import GithubApiCrawlerItem

class UserApiSpider(scrapy.Spider):
    name = 'user_api'
    allowed_domains = ['github.com/users']

    start_urls = [l.strip() for l in open('/usr/src/app/urls_trim.txt').readlines()]

    def parse(self, response):

        # api_limit_response = scrapy.Request(url='https://api.github.com/rate_limit',method='GET')
        #
        # json_rate_limit = json.loads(api_limit_response)
        #
        # rate_limit = json_rate_limit["resources"]["core"]["limit"]
        # print("____________________" + rate_limit + "______________________")

        jsonresponse = json.loads(response.body_as_unicode())

        item = GithubApiCrawlerItem()
        item["username"] = jsonresponse["login"]
        item["id"] = jsonresponse["id"]
        item["node_id"] = jsonresponse["node_id"]
        item["avatar_url"] = jsonresponse["avatar_url"]
        item["gravatar_id"] = jsonresponse["gravatar_id"]
        item["url"] = jsonresponse["url"]
        item["html_url"] = jsonresponse["html_url"]
        item["followers_url"] = jsonresponse["followers_url"]
        item["following_url"] = jsonresponse["following_url"]
        item["gists_url"] = jsonresponse["gists_url"]
        item["starred_url"] = jsonresponse["starred_url"]
        item["subscriptions_url"] = jsonresponse["subscriptions_url"]
        item["organizations_url"] = jsonresponse["organizations_url"]
        item["repos_url"] = jsonresponse["repos_url"]
        item["events_url"] = jsonresponse["events_url"]
        item["received_events_url"] = jsonresponse["received_events_url"]
        item["type"] = jsonresponse["type"]
        item["site_admin"] = jsonresponse["site_admin"]
        item["name"] = jsonresponse["name"]
        item["company"] = jsonresponse["company"]
        item["blog"] = jsonresponse["blog"]
        item["location"] = jsonresponse["location"]
        item["email"] = jsonresponse["email"]
        item["hireable"] = jsonresponse["hireable"]
        item["bio"] = jsonresponse["bio"]
        item["public_repos"] = jsonresponse["public_repos"]
        item["public_gists"] = jsonresponse["public_gists"]
        item["followers"] = jsonresponse["followers"]
        item["following"] = jsonresponse["following"]
        item["created_at"] = jsonresponse["created_at"]
        item["updated_at"] = jsonresponse["updated_at"]

        yield item


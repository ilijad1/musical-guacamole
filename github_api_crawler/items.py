# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GithubApiCrawlerItem(scrapy.Item):

    username = scrapy.Field()
    id = scrapy.Field()
    node_id = scrapy.Field()
    avatar_url = scrapy.Field()
    gravatar_id = scrapy.Field()
    url = scrapy.Field()
    html_url = scrapy.Field()
    followers_url = scrapy.Field()
    following_url = scrapy.Field()
    gists_url = scrapy.Field()
    starred_url = scrapy.Field()
    subscriptions_url = scrapy.Field()
    organizations_url = scrapy.Field()
    repos_url = scrapy.Field()
    events_url = scrapy.Field()
    received_events_url = scrapy.Field()
    type = scrapy.Field()
    site_admin = scrapy.Field()
    name = scrapy.Field()
    company = scrapy.Field()
    blog = scrapy.Field()
    location = scrapy.Field()
    email = scrapy.Field()
    hireable = scrapy.Field()
    public_repos = scrapy.Field()
    bio = scrapy.Field()
    public_gists = scrapy.Field()
    followers = scrapy.Field()
    following = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()


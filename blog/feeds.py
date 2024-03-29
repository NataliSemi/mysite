from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatechars(item.body, 30)

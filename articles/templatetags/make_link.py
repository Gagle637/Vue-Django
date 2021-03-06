from django import template

register = template.Library()

@register.filter
def hashtag_link(word):
    content = word.content + ' '
    hashtags = word.hashtags.all()
    for hashtag in hashtags:
        content = content.replace(hashtag.content+' ', f'<a href="/articles/" @click="back_method(`{hashtag}`)">{ hashtag.content }</a> ')
    return content

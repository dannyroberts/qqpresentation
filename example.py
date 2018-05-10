def get_all_posts(person):
    cache_key = 'get_all_posts:{}'.format(person.id)
    posts = cache.get(cache_key, default=None)
    if posts is None:
        posts = Post.objects.filter(person=person).all()
        cache.set(cache_key, posts)
    return posts

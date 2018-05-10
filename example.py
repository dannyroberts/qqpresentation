def get_all_posts_cache_key(person):
    return 'get_all_posts:{}'.format(person.id)


def clear_all_posts_cache(person):
    cache_key = get_all_posts_cache_key(person)
    cache.delete(cache_key)


def get_all_posts(person):
    cache_key = get_all_posts_cache_key(person)
    posts = cache.get(cache_key, default=None)
    if posts is None:
        posts = Post.objects.filter(person=person).all()
        cache.set(cache_key, posts)
    return posts

from quickcache.django_quickcache import get_django_quickcache

quickcache = get_django_quickcache(timeout=5 * 60, memoize_timeout=0)


@quickcache(['person.id'])
def get_all_posts(person):
    return Post.objects.filter(person=person).all()

from quickcache.django_quickcache import get_django_quickcache

quickcache = get_django_quickcache(timeout=5 * 60, memoize_timeout=0)


@quickcache(['person.id'], skip_arg='strict', timeout=60 * 60)
def get_all_posts(person, strict=False):
    return Post.objects.filter(person=person).all()

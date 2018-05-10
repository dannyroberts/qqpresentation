def get_all_posts(person):
    return Post.objects.filter(person=person).all()

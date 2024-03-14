blogs = dict()
from blog import Blogs

def menu():
    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
blogs = dict()
from blog import Blogs

menu_prompt = "Enter c to create a blog, 'l' to list blogs, 'r' to read one, p to post, q to quit"

def menu():
    print_blogs()
    selection = input(menu_prompt)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
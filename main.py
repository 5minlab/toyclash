#!/usr/bin/env/python

"""
https://gist.github.com/wrunk/1317933
"""

from jinja2 import Environment

from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(THIS_DIR, "templates")
OUTPUT_DIR = os.path.join(THIS_DIR, "docs")

def main():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                         trim_blocks=True)
    write_html(j2_env, "index.j2", "index.html")
    write_html(j2_env, "press.j2", "press.html")

def write_html(env, template_file, output_file):
    html = env.get_template(template_file).render(
        title='this is title'
    )
    f = open(os.path.join(OUTPUT_DIR, output_file), "w")
    f.write(html)


if __name__ == '__main__':
    main()

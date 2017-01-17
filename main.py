#!/usr/bin/env/python

"""
https://gist.github.com/wrunk/1317933
"""

import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(THIS_DIR, "templates")
CONTENT_DIR = os.path.join(THIS_DIR, "contents")
OUTPUT_DIR = os.path.join(THIS_DIR, "docs")

def md_file_to_html(filepath):
    src = open(filepath, encoding="utf-8").read()
    return markdown.markdown(src, extensions=['markdown.extensions.tables'])

def main():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
                         trim_blocks=True)
    write_html(j2_env, "index.j2", "index.html")

    game_info = md_file_to_html(os.path.join(CONTENT_DIR, "game_info.md"))
    team_info = md_file_to_html(os.path.join(CONTENT_DIR, "team_info.md"))

    write_html(j2_env, "press.j2", "press/en/index.html",
        press_html=md_file_to_html(os.path.join(CONTENT_DIR, "press_en.md")),
        game_info_html=game_info,
        team_info_html=team_info,
        locale="en",
        game_info_title="Game Assets",
        team_info_title="Team Photo",
    )

    write_html(j2_env, "press.j2", "press/ko/index.html",
        press_html=md_file_to_html(os.path.join(CONTENT_DIR, "press_ko.md")),
        game_info_html=game_info,
        team_info_html=team_info,
        locale="ko",
        game_info_title="게임 자료",
        team_info_title="팀 사진",
    )

def write_html(env, template_file, output_file, **kwargs):
    html = env.get_template(template_file).render(**kwargs)
    output_filepath = os.path.join(OUTPUT_DIR, output_file)
    output_path = os.path.dirname(output_filepath)
    try:
        os.makedirs(output_path, exist_ok=True)
    except OSError:
        pass

    open(output_filepath, mode="w", encoding="utf-8").write(html)

if __name__ == '__main__':
    main()

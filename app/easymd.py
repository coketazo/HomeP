import markdown
import os


def markdown_to_html(md_file_path) -> str:
    with open(md_file_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content)

    return html_content


def markdown_files_to_html_dict(name) -> dict:
    # 기본 md파일 디렉토리 / name /
    md_dir = "./static/md/" + name + "/"
    # 디렉토리 안의 파일 리스트
    md_file_list = os.listdir(md_dir)
    # list -> dict
    md_file_dict = {
        f"section{i}": md_dir + md_file_list[i] for i in range(len(md_file_list))
    }

    # 각 Markdown 파일을 HTML로 변환
    sections_html_dict = {
        section: markdown_to_html(md_path) for section, md_path in md_file_dict.items()
    }

    return sections_html_dict

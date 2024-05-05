import markdown
from flask import Flask, render_template

app=Flask(__name__)


def markdown_to_html(md_file_path):
	with open(md_file_path, 'r',encoding='utf-8') as f:
		md_content=f.read()
	html_content=markdown.markdown(md_content)
	return html_content

@app.route("/",methods=["GET"])
def home():
	md_loc = './static/md/'
	md_files = {
        'section1': md_loc + 'About_Us.md',
        'section2': md_loc + 'Events.md',
        'section3': md_loc + 'Member.md',
		'section4': md_loc + 'Blog.md',
		'section5': md_loc + 'Resources.md',
		'section6': md_loc + 'Contact.md'
    }
    # 각 Markdown 파일을 HTML로 변환
	sections_html = {
		section: markdown_to_html(md_path) for section, md_path in md_files.items()
	}
	
	return render_template('test.html', sections=sections_html)

if __name__ == '__main__':
	app.run(debug=True)
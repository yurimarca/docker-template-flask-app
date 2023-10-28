from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, visit /render to render the LaTeX file.'

@app.route('/render')
def render_latex():
    latex_code = r'''
    \documentclass{article}
    \begin{document}
    Hello, this is a simple LaTeX document.
    \end{document}
    '''
    with open('temp.tex', 'w') as f:
        f.write(latex_code)

    try:
        subprocess.run(['pdflatex', 'temp.tex'], check=True)
    except subprocess.CalledProcessError:
        return 'Failed to compile LaTeX'

    for ext in ['.aux', '.log']:
        os.remove(f'temp{ext}')

    return send_file('temp.pdf', as_attachment=True, download_name='rendered.pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

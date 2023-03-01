from portrait import portrait
import os
from flask import (
     Flask, 
     request, 
     render_template)

from create import waifu_diffusion

portrait_path='./static/portrait/portrait.jpg'
waifu_diffusion_path='./static/diffusion/waifu.jpg'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portrait')
def p1():
    return  render_template('portrait.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        output=portrait(upload_file)
        output.save(portrait_path)
        return render_template('portrait_result.html' , portrait_path =portrait_path)

    
@app.route('/diffusion')
def p2():
    return  render_template('diffusion.html')

@app.route('/result', methods=['GET', 'POST'])
def prompt():
    if request.method == 'POST':
        prompt =  request.form.get('item')
        print(prompt)
        output=waifu_diffusion(prompt)
        output.save(waifu_diffusion_path)
        return render_template('diffusion_result.html', waifu_diffusion_path =waifu_diffusion_path)


if __name__ == "__main__":
    app.run(debug=True)
from portrait import portrait
import os
from flask import (
     Flask, 
     request, 
     render_template)



UPLOAD_FOLDER='./static/modnet_image/input'
portrait_path='./static\modnet_image\output/portrait.jpg'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portrait')
def product01():
    return  render_template('portrait.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        img_path = 'static\modnet_image\input\\22861417_s.jpg'# os.path.join(UPLOAD_FOLDER,upload_file.filename)
        upload_file.save(img_path)
        output=portrait(img_path)
        # output.save(portrait_path)
        # print(portrait_path)
    return render_template('portrait_result.html',portrait_path=output)

if __name__ == "__main__":
    app.run(debug=True)
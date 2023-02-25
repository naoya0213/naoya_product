from portrait import portrait
import os
from flask import (
     Flask, 
     request, 
     render_template)
from werkzeug.utils import secure_filename


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
        # img_path = 'static\modnet_image\input\\22861417_s.jpg'# os.path.join(UPLOAD_FOLDER,upload_file.filename)
        # upload_file.save(img_path)
        # output=portrait(img_path)
        # output.save(portrait_path)
        # print(portrait_path)
        
        f = secure_filename(upload_file.filename)
        path_2_tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        print(os.path.join(path_2_tmp, f))
        if not os.path.exists(path_2_tmp):
            os.mkdir(path_2_tmp)
        f.save(os.path.join(path_2_tmp, f))
        return f
    return render_template('portrait_result.html',portrait_path=os.path.join(path_2_tmp, f))

@app.route('/image-upload', methods=['GET', 'POST'])
def image_post():
    if request.method == 'POST':
        f = request.files['file']
        
        return "file req error"
    return "post error"

# @app.route('/fetch-image', methods=['GET', 'POST'])
# def fetch_image():
#     if request.method == 'GET':
#         for fn in glob.glob(os.path.join(os.getcwd(),"tmp","*")):
#             print(fn)
#     return "fetch image"


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,render_template,request,redirect
from werkzeug.utils import secure_filename
import os
from DECIMER import predict_SMILES


application = Flask(__name__)
application.config['IMAGE_UPLOADS'] = '/home/iiitd/decimer/static/images'
@application.route("/home",methods = ['POST','GET'])
def upload_image():
 if request.method == "POST":
   image = request.files['file']
   if image.filename == '':
     print("Filename is invalid")
     return redirect(request.url)
   
   filename = secure_filename(image.filename)
   
   basedir = os.path.abspath(os.path.dirname(__file__))
   image.save(os.path.join(basedir,application.config['IMAGE_UPLOADS'],filename))
   #image_path = url_for('static',filename='/images/'+filename);
   SMILES = predict_SMILES(os.path.join(basedir,application.config['IMAGE_UPLOADS'],filename))
   print(SMILES)
   return render_template("index.html",filename = filename,smile = SMILES)
    
 return render_template("index.html")
 
@application.route('/display/<filename>')
def display_image(filename):
 return redirect(url_for('static',filename='/images/'+filename),code=301)
application.run(port = 5001)

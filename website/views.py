#where we store the routes that a user can go to (ex: home page, test page)
import os
import extraction_new
from flask import Blueprint, render_template, request, flash, redirect, send_file


views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST']) #route for the home page. This function will run every time we go to the '/' route
def home():
    if request.method == 'POST':
        f = request.files['file']
        f.save('user_upload.pdf')
        if f.mimetype != "application/pdf":
            flash('Uploaded file must be a PDF', category='error')
        else:
            extraction_new.main()
            return redirect('/uploaded')

    return render_template("home.html")

@views.route('/uploaded')
def uploaded():
    return render_template("uploaded.html")

@views.route('/instructions')
def instructions():
    return render_template("instructions.html")

@views.route('/uploaded/download')
def download():
    path = '../calendar.csv'
    return send_file(path, as_attachment=True)







from flask import Flask, render_template, url_for, redirect, request
import os
import PyPDF2
from werkzeug.wrappers import Request, Response
from tika import parser
pdfUse =  0
app = Flask(__name__)
app.config["pdfUpload"] = (r"C:\Users\johnn\Hack4PanProject")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        if request.files:

            global pdf
            pdf = request.files["myFile"]
            
            
            pdf.save(os.path.join(app.config["pdfUpload"], pdf.filename))
            global pdfUse
            pdfUse = pdf.filename
            print(pdfUse)
            print(pdf)
            return redirect(request.url)
    return render_template("index.html")


print(pdfUse)



if __name__ == "__main__":
    app.run(debug=True) 
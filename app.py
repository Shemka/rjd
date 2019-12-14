import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from pdf2npcols import pdf2npcols
from numdetect import col2nums
from ledetect import col2lets
from tensor2dfs import tensor2dfs
import zipfile

app = Flask(__name__)
uploads_dir = os.path.join(app.instance_path, 'uploads')

@app.route("/", methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    if request.method == "POST":
        # тебе надо  для нескольких pdfов и для нескольких файлов собрать матрицы (колонки)
        file = request.files[archive]
        args["method"] = "POST"
        
        file = Danil.file(file).save(os.path.join(uploads_dir, secure_filename(file.name+'.pdf')))
        cols = pdf2npcols('instance/uploads/pdf_file.pdf')  # нампи массив с нормализованными картинками
        matrix = [col2nums(col) for col in cols]
        tensor = [matrix] # тензор - несколько матриц для разных пдф файлов
        dfs = tensor2dfs(tensor)

        #  dfs  мы передаем Саше 

        return send_file('instance/uploads/pdf_file.pdf', as_attachment=True)
    return render_template("index.html", args=args)

if __name__ == '__main__':
    #os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)
    app.run()

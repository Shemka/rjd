import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from pdf2cols import pdf2npcols
from numdetect import col2nums
from letdetect import col2lets
from tensor2dfs import tensor2dfs
from exstruct_zip import zip2pdf

app = Flask(__name__)
uploads_dir = os.path.join(app.instance_path, 'uploads')

@app.route("/", methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    if request.method == "POST":
        # тебе надо  для нескольких pdfов и для нескольких файлов собрать матрицы (колонки)
        print('enter')
        print(list(request.files.items()))
        file = request.files["archive"]
        args["method"] = "POST"
<<<<<<< HEAD
        
        file = Danil.file(file).save(os.path.join(uploads_dir, secure_filename(file.name+'.pdf')))
        cols = pdf2npcols('instance/uploads/pdf_file.pdf')  # нампи массив с нормализованными картинками
        matrix = [col2nums(col) if i != 1 else col2lets(col) for i, col in enumerate(cols)]
        tensor = [matrix] # тензор - несколько матриц для разных пдф файлов
        dfs = tensor2dfs(tensor)

=======
        file = file.save(os.path.join(uploads_dir, secure_filename(file.name+'.pdf')))
        zip2pdf("archive.pdf")
        spisock = []
        schet = 0
        for pdf_name in os.listdir('pdf_file'):
            spisock.append([])
            cols = pdf2npcols('pdf_file/'+pdf_name)  # нампи массив с нормализованными картинками
            spisock[schet].append(col2nums(cols[0],False,True,False))
            spisock[schet].append(col2lets(cols[1]))
            spisock[schet].append(col2nums(cols[2],False,False,True))
            spisock[schet].append(col2nums(cols[3],True,False,False))
            spisock[schet].append(col2nums(cols[4],False,False,False))
            schet+=1
        print(spisock)
        dfss = tensor2dfs(a)
        dfs = [df.transpose() for df in dfss]
>>>>>>> 539a75555a14e657e4c3a1c78c309ca7e85a1da6
        #  dfs  мы передаем Саше 

        #return send_file('instance/uploads/pdf_file.pdf', as_attachment=True)
    return render_template("site/index.html", args=args)

if __name__ == '__main__':
    #os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)
    app.run(debug=True)

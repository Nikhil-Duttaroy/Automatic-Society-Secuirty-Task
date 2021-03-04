from flask import Flask, render_template,request
import face_recognition
import face_training
import face_dataset
import irregular_dataset
import sqlite3

    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    result=db.session.query(Users).all()
    for r in result:
        print(result)

@app.route('/addtodataset' , methods=["Get","POST"])
def addtodataset():
    if request.method == "POST": 
       global Name
       Name= request.form.get("Name")  
       global Flat
       Flat= request.form.get("Flat")  
       Type=request.form.get("Type")
       con = sqlite3.connect('FaceBase.db')
       print(Name)
       c =  con.cursor() 
       cmd="INSERT INTO Users(Name,Flat,Type) Values(?,?,?);"
       con.execute(cmd,(Name,Flat,Type))
       con.commit()
       con.close() 
       face_dataset.data()

    return render_template("addtodataset.html") 
  
@app.route('/irregular' , methods=["Get","POST"])
def irregular():
    if request.method == "POST": 
       Name= request.form.get("Name")  
       Phone= request.form.get("Phone")  
       Visit= request.form.get("Visit")  
       Purpose= request.form.get("Purpose")
       con = sqlite3.connect('FaceBase.db')
       print(Name)
       c =  con.cursor() 
       cmd="INSERT INTO Irregular(Name,Phn,Visit,Purpose,Time) Values(?,?,?,?,datetime('now','localtime'));"
       con.execute(cmd,(Name,Phone,Visit,Purpose))
       con.commit()
       con.close() 
       irregular_dataset.data()

    return render_template("irregular.html") 


@app.route('/admin')
def admin():
   return render_template('admin.html')

@app.route('/train')
def train():
    face_training.train()
    print("Training Done")
    return render_template('index.html')


@app.route('/recognize')
def parse1():
    face_recognition.reco()
    print("Reconn Done")
    return render_template('index.html')
    

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
    
from flask import Flask, render_template,request,redirect,url_for
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
       return redirect(url_for('admin'))

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
       cmd="INSERT INTO Irregular(Name,Phn,Visit,Purpose,EntryTime) Values(?,?,?,?,datetime('now','localtime'));"
       con.execute(cmd,(Name,Phone,Visit,Purpose))
       con.commit()
       con.close() 
       irregular_dataset.irrdata()
       return redirect(url_for('index'))

    return render_template("irregular.html") 


@app.route('/adminlogin', methods=["Get","POST"])
def adminlogin():
    if request.method == "POST": 
       message=""
       Username= request.form.get("username")  
       Password= request.form.get("password")  
       if (Username=="admin" and Password=="1234"):
           return render_template('admin.html')
       else:
           message="Incorrect Credentails"
           return render_template('adminlogin.html',message=message)
    return render_template('adminlogin.html')


@app.route('/admin')
def admin():
   return render_template('admin.html')

@app.route('/details')
def details():
    conn=sqlite3.connect("FaceBase.db")
    cmd="Select * from Users;"
    cursor=conn.execute(cmd)
    cursor.execute(cmd)
    conn.commit()
    data=cursor.fetchall()
    return render_template("details.html",data=data)     
    
@app.route('/irrdetails')
def irrdetails(): 
    conn=sqlite3.connect("FaceBase.db")
    cmd1="Select * from Irregular;"
    cursor=conn.execute(cmd1)
    cursor.execute(cmd1)
    conn.commit()
    irrdata=cursor.fetchall()
    conn.close()
    return render_template("irrdetails.html",irrdata=irrdata)


@app.route('/train')
def train():
    face_training.train()
    print("Training Done")
    return render_template('admin.html')


@app.route('/recognize')
def parse1():
    face_recognition.reco()
    print("Reconn Done")
    return render_template('index.html')
    

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
    

from flask import Flask,render_template,request,jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/postdata',methods=['POST'])
def submit():
    if request.method == 'POST':
        fn=request.form["firstname"]
        ln = request.form["lastname"]
        print(fn,ln)
        ABC = fn + ln + "Submitted Succesfully"

        return ABC
    else:
        return "Something Went Wrong"




@app.route("/get-user01",methods=['GET'])
def get_user1():
    if request.method == 'GET':
        userData={
            "userId": "shivraj_s",
            "name": "Shivraj",
            "email":"shindeshivraj@example.com"
        }
            
        return jsonify(userData), 200
    else:
        return "Something went Wrong"






@app.route("/get-user/<userId>")
def get_user(userId):
    
    userData={
        "userId": userId,
        "name": "Shivraj",
        "email":"shindeshivraaj@gmail.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        userData["extra"] = extra
        
    return jsonify(userData), 200




if __name__ == "__main__":
    app.run(debug=True)
    
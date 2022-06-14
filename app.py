from importlib import resources
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "Secret Key"


static_db= []

global_id = 0

def generate_id():
    global global_id
    global_id +=  1
    return global_id



@app.route('/')
def Index():
    return render_template("index.html", Resources = static_db)


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        global static_db

        Name = request.form['name']
        tags = request.form['tags']
        level = request.form['level']
        types = request.form['type']

        static_db.append({'id': generate_id() ,'name':Name, 'tags': tags, 'level': level , 'type': types})
        print(static_db)

        flash("Resource Added Successfully")

        return redirect(url_for('Index'))


#This route is for editing our resource
@app.route('/update', methods = ['GET', 'POST'])
def update():    

    if request.method == 'POST':     
        global static_db   
        user_id = request.form.get('id')
        print(type(user_id))
        print(static_db)
        my_data = [i for i in static_db if i['id'] == int(user_id)][0]
        print(my_data)
        my_data['name'] = request.form['name']
        my_data['tags'] = request.form['tags']
        my_data['level'] = request.form['level']
        my_data['type'] = request.form['type']

        flash("Resource Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting our resource
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    global static_db
    my_data = [i for i in range(len(static_db)) if static_db[i]['id'] == int(id)][0]
    static_db.pop(my_data)
    flash("Resource Deleted Successfully")

    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
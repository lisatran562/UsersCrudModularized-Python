from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route('/')
@app.route('/users')
def index():
    users = User.get_all()

    return render_template('index.html', users=users)


@app.route('/users/new')
def user_new():
    return render_template('create.html')

@app.route('/users/new', methods=['POST'])
def create():
    User.save(request.form)

    return redirect('/')

@app.route('/users/<int:id>')
def show_user(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template('show.html', user=user)

@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)

@app.route('/users/edit', methods=['POST'])
def update_user():
    User.update_one(request.form)
    print(request.form)
    id = request.form['id']
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/delete')
def destroy(id):
    data = {
        'id': id
    }
    User.delete_one(data)

    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)
     
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    check = db.Column(db.Boolean, default=False)

    def __repl__(self):
        return 'Task <%r>' % self.id

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form.get("task_content", False)
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Some problems with creating'
    
    tasks = Todo.query.order_by(Todo.check.asc(), Todo.date_created.asc()).all()
    return render_template('list.html', tasks=tasks)

@app.route('/check/<int:id>')
def check(id):
    ttc = Todo.query.get_or_404(id) #task to check
    try:
        ttc.check = True
        db.session.commit()
        return redirect('/')
    except:
        return 'Some problems with checking'
    
@app.route('/uncheck/<int:id>')
def uncheck(id):
    ttuc = Todo.query.get_or_404(id) #task to uncheck
    try:
        ttuc.check = False
        db.session.commit()
        return redirect('/')
    except:
        return 'Some problems with unchecking'

@app.route('/delete/<int:id>')
def delete(id):
    ttd = Todo.query.get_or_404(id) #task to delete
    try:
        db.session.delete(ttd)
        db.session.commit()
        return redirect('/')
    except:
        return 'Some problems with deleting'

@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        tte = Todo.query.get_or_404(id) #task to edit
        try:
            tte.content = request.form.get("task_content", False)
            db.session.commit()
            return redirect('/')
        except:
            return 'Some problems with editing'
    
    tte = Todo.query.get_or_404(id)
    return render_template('edit.html', id = tte.id, task = tte)

if __name__ == '__main__':
    app.run()
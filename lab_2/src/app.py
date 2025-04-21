from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER', 'postgres')}:{os.getenv('POSTGRES_PASSWORD', 'root')}@{os.getenv('POSTGRES_HOST', 'postgres1')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DB', 'flask_db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


@app.route('/')
def index():
    try:
        data = Product.query.all()
        return render_template('index.html', data=data)
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return render_template('error.html', message="Ошибка загрузки данных")

@app.route('/create', methods=['POST'])
def create():
    try:
        name = request.form['name']
        price = float(request.form['price'])
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Ошибка при создании записи: {e}")
        db.session.rollback()
        return render_template('error.html', message="Ошибка создания записи")

@app.route('/update', methods=['POST'])
def update():
    try:
        id = int(request.form['id'])
        product = Product.query.get(id)
        if product:
            product.name = request.form['name']
            product.price = float(request.form['price'])
            db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Ошибка при обновлении записи: {e}")
        db.session.rollback()
        return render_template('error.html', message="Ошибка обновления записи")

@app.route('/delete', methods=['POST'])
def delete():
    try:
        id = int(request.form['id'])
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Ошибка при удалении записи: {e}")
        db.session.rollback()
        return render_template('error.html', message="Ошибка удаления записи")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

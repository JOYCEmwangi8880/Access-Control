from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import text





db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///access_control.db'
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'



    @app

    

    @app.route('/')
    def home():
        return render_template('home.html')
    

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        return render_template('register.html')


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('login.html')



    @login_manager.user_loader
    def load_user(user_id):
        return None


    return app




if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
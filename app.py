from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import text





db = SQLAlchemy()
login_manager = LoginManager()



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'
    




def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///access_control.db'
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'



    @app.route("/access/db")
    def access_db():
        try:
            db.session.execute(text("SELECT 1"))
            return {"db": "ok"}, 200
        except Exception as e:
            return {"db": "error", "details": str(e)}, 500
        


    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return render_template('home.html')
    

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')


            print("form submitted", username, email, password, confirm_password)
            return f"received data - {email}"

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
from flask import Flask, session, g
import config
from exts import db, mail
from blueprints import qa_bp, user_bp
from flask_migrate import Migrate
from models import UserModel

app = Flask(__name__)
# 绑定
app.config.from_object(config)
# 初始化
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

# 注册
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个叫做user的变量，他的值是user这个变量
            # setattr(g, 'user', user)
            g.user = user
        except:
            g.user = None


# 请求来了 -> before_request -> 视图函数 -> 视图函数中返回模板 -> context_processor
@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run(debug=True)

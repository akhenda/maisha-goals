import os
from app import create_app, db
from app.models import User

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
    with app.app_context():
        db.create_all()
        # create a development user
        if User.query.get(1) is None:
            u = User(username='john')
            u.set_password('cat')
            db.session.add(u)
            db.session.commit()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

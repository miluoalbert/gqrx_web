import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import dashboard
    app.register_blueprint(dashboard.bp)
    app.add_url_rule('/', endpoint='index')

    return app

if __name__ == '__main__':
  app = Flask(__name__, instance_relative_config=True)
  from . import dashboard
  app.register_blueprint(dashboard.bp)
  app.add_url_rule('/', endpoint='index')
  app.run(host='0.0.0.0', port=5080)

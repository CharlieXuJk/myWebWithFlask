from app import create_app

app = create_app()

if __name__ == '__main__':
    #生产环境 nginx+uwsgi,生产环境下不会启动flask自带的服务器
    app.run(debug=app.config['DEBUG'])
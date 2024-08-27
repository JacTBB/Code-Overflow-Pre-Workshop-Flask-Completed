from app.config import Config
from app import create_app


app = create_app(Config)

if __name__ == '__main__':
    app.run(port=3000, debug=True)

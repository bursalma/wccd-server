from dotenv import load_dotenv

from flaskr import create_app

load_dotenv()
app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

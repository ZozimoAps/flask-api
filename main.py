from app import create_app
from settings import environment

develop = environment.get(
    'develop', 
    'No existe este entorno'
)

app = create_app(develop)

if __name__ == '__main__':
    app.run()
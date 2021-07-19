from . import db, ma
from sqlalchemy import event


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description


def insert_tasks(*args, **kwargs):
    first_task = Task(
        title='Preparar comida',
        description='Para la cena'
    )
    db.session.add(first_task)
    db.session.commit()

event.listen()


class TaskSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

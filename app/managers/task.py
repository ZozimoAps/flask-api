from flask import request
from app.responses import bad_request, success_response
from app.models import db
from app.models.task import Task, task_schema, tasks_schema


def save_task_api(title, description):
    new_title = title
    new_description = description

    if new_title is None:
        return bad_request()
    elif len(new_title) == 0 or len(new_title) > 50:
        return bad_request()

    if new_description is None:
        return bad_request()
    elif len(new_description) == 0:
        return bad_request()

    data = Task(
        title=new_title,
        description=new_description
    )
    db.session.add(data)
    db.session.commit()
    return task_schema.jsonify(data), 201


def all_tasks():
    tasks = Task.query.order_by(Task.id).all()
    return success_response(
        data=tasks_schema.dump(tasks)
    )


def task_by_id(*args):
    task = Task.query.filter_by(id=args).first()
    return success_response(
        data=task_schema.dump(task)
    )


def task_update(*args):
    task = Task.query.get(args)
    task.title = request.json['title']
    task.description = request.json['description']
    db.session.commit()
    return task_schema.jsonify(task), 201


def delete_task(*args):
    task = Task.query.get(args)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task), 200

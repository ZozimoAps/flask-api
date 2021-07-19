from flask import Blueprint, request
from app.managers.task import save_task_api, all_tasks, task_by_id, task_update, delete_task


api_v1 = Blueprint(
    'api',
    __name__,
    url_prefix='/api/v1'
)


@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    return all_tasks()


@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    return task_by_id(id)


@api_v1.route('/tasks/add', methods=['POST'])
def add_task():
    return save_task_api(
        title=request.json.get('title', None),
        description=request.json.get('description', None)
    )


@api_v1.route('/tasks/update/<id>', methods=['PUT'])
def update_task(id):
    return task_update(id)


@api_v1.route('/tasks/delete/<id>', methods=['DELETE'])
def destroy_task(id):
    return delete_task(id)

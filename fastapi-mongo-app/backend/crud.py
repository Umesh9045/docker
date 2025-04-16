from database import db
from bson import ObjectId
from database import task_collection


def get_all_tasks():
    return list(task_collection.find({}, {"_id": 0}))

def create_task(task_data):
    task_collection.insert_one(task_data)
    return {"msg": "Task created"}

def get_priority_summary():
    pipeline = [
        {
            "$group": {
                "_id": "$priority",  # group by priority
                "total_tasks": { "$sum": 1 },
                "tasks": {
                    "$push": {
                        "name": "$name",
                        "priority": "$priority"
                    }
                }
            }
        },
        { "$sort": { "_id": 1 } }
    ]

    summary = list(task_collection.aggregate(pipeline))
    return summary


def update_task(name, new_data):
    result = task_collection.update_one(
        {"name": name},
        {"$set": new_data}
    )
    if result.matched_count:
        return {"msg": "Task updated"}
    return {"msg": "Task not found"}


def delete_task(name):
    result = task_collection.delete_one({"name": name})
    if result.deleted_count:
        return {"msg": "Task deleted"}
    return {"msg": "Task not found"}

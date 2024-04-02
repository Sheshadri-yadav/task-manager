from sqlalchemy import text

from config.db import engine


def all_tasks():
    with engine.connect() as connection:
        # Execute your query
        query = text("SELECT * FROM tasks")
        result = connection.execute(query)

        results_return = []

        for row in result:
            task_id = row[0]
            task_title = row[1]
            task_desc = row[2]
            due_date = row[3]
            due_time = str(row[4])
            task_status = "Incomplete" if row[5] == False else "Completed"

            modified_row = {
                "task_id": task_id,
                "task_title": task_title,
                "task_desc": task_desc,
                "due_date": due_date,
                "due_time": due_time,
                "task_status": task_status
            }

            results_return.append(modified_row)

        return results_return




def insert_query(title, desc, due_date, due_time, status):
    with engine.connect() as connection:
        # Execute your query

        # Properly format the SQL query string with placeholders and use parameters to prevent SQL injection
        query = text(
            "INSERT INTO tasks (task_title, task_desc, due_date, due_time, task_status) "
            "VALUES (:task_title, :task_desc, :due_date, :due_time, :task_status)"
        )
        # Execute the query with parameters
        result = connection.execute(query, {

            'task_title': title,
            'task_desc': desc,
            'due_date': due_date,
            'due_time': due_time,
            'task_status': status
        })
        connection.commit()


def completed_tasks():
    with engine.connect() as connection:
        # Execute your query
        query = text("Select * from tasks where task_status =True")
        result = connection.execute(query)
        results_return = []
        # Fetch the results if needed
        for row in result:
            results_return.append(row)

        return results_return


def incomplete_tasks():
    with engine.connect() as connection:
        # Execute your query
        query = text("Select * from tasks where task_status =False")
        result = connection.execute(query)
        results_return = []
        # Fetch the results if needed
        for row in result:
            results_return.append(row)

        return results_return


def update_tasks(task_id: int):
    with engine.connect() as connection:
        query = text("Update tasks set task_status =true where task_id =:id")
        result = connection.execute(query, {
            'id': task_id
        })
        connection.commit()


def delete_task(task_id: int):
    with engine.connect() as connection:
        query = text("delete from tasks  where task_id =:id")
        result = connection.execute(query, {
            'id': task_id
        })
        connection.commit()



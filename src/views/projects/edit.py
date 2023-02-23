from models.Project import Project
from playhouse.shortcuts import model_to_dict
import pandas as pd


project_id = __query_params__["id"]
project = Project.get_by_id(project_id)


def update_project():
    project.save()
    __redirect__("views/customers/edit", {"id": project.customer_id})

board = {
    "type": "kanban-board",
    "stages": [
        {
            "type": "kanban-stage",
            "name": m.name,
            "cards": [
                {
                    "type": "kanban-card",
                    "name": t.name,
                    "description": t.description,
                    "tags": [],
                } for t in m.tasks
            ]
        } for m in project.milestones
    ]
}
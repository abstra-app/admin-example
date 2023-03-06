from models.Project import Project
from playhouse.shortcuts import model_to_dict
import pandas as pd
from abstra.dashes import redirect, query_params


project_id = query_params["id"]
project = Project.get_by_id(project_id)


def update_project():
    project.save()
    redirect("views/customers/edit", {"id": project.customer_id})

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
from api.db import db
from models.Customer import Customer
from models.Project import (
    Project,
    ProjectMilestone,
    ProjectMilestoneTask,
    ProjectMilestoneTaskDependency,
)
from faker import Faker
import random

fake = Faker()


def run():
    db.create_tables(
        [
            Customer,
            Project,
            ProjectMilestone,
            ProjectMilestoneTask,
            ProjectMilestoneTaskDependency,
        ]
    )

    for _ in range(10):
        customer = Customer.create(
            name=fake.name(),
            ein=fake.ein(),
            email=fake.company_email(),
            phone=fake.phone_number(),
            country=fake.country(),
            zip=fake.zipcode(),
            address=fake.address(),
        )

        for _ in range(random.randint(5, 10)):
            project = Project.create(name="Test Project", customer=customer)
            milestone = ProjectMilestone.create(
                name=fake.text(20),
                project=project,
                description=fake.paragraph(),
                deadline=fake.date_time(),
            )
            ProjectMilestoneTask.create(
                name=fake.text(20),
                description=fake.paragraph(),
                deadline=fake.date_time(),
                start=fake.date_time(),
                end=fake.date_time(),
                project_milestone=milestone,
            )

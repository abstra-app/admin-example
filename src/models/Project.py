import peewee as pw
from models.Base import Base
from models.Customer import Customer


class Project(Base):
    name = pw.CharField()
    customer = pw.ForeignKeyField(Customer, backref="projects")


class ProjectMilestone(Base):
    project = pw.ForeignKeyField(Project, backref="milestones")
    name = pw.CharField()
    description = pw.CharField()
    deadline = pw.DateTimeField()


class ProjectMilestoneTask(Base):
    project_milestone = pw.ForeignKeyField(ProjectMilestone, backref="tasks")
    name = pw.CharField()
    description = pw.CharField()
    deadline = pw.DateTimeField()
    start = pw.DateTimeField(null=True)
    end = pw.DateTimeField(null=True)


class ProjectMilestoneTaskDependency(Base):
    task = pw.ForeignKeyField(ProjectMilestoneTask, backref="dependencies")
    dependency = pw.ForeignKeyField(ProjectMilestoneTask, backref="dependents")

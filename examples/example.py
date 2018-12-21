from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from sqlavisualizer import DBRepresentation

BASE = declarative_base()


class User(BASE):
    __tablename__ = 'user_table'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50))


class Course(BASE):
    __tablename__ = 'course_table'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(50))
    description = Column(Unicode(200))


class Module(BASE):
    __tablename__ = 'module_table'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(50))
    description = Column(Unicode(200))
    course_id = Column(Integer, ForeignKey('course_table.id'))


class Unit(BASE):
    __tablename__ = 'unit_table'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(50))
    description = Column(Unicode(200))
    module_id = Column(Integer, ForeignKey('module_table.id'))


class CourseRegistration(BASE):
    __tablename__ = 'registration_table'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_table.id'))
    course_id = Column(Integer, ForeignKey('course_table.id'))


models = [User, Course, Module, Unit, CourseRegistration]
db_repr = DBRepresentation(models)

dot_repr = db_repr.to_dot()

with open('example.dot', 'w') as f:
    f.write(dot_repr)

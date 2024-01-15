from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Group  # Import your models
from models import Professor
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Base.metadata.create_all(engine)

# ... (other model definitions)

# Your group creation code
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker object
fake = Faker()


# Function to add a group to the database
def add_group(name):
    group = Group(g_name=name)
    session.add(group)


# Add three groups
group_names = ["Group A", "Group B", "Group C"]
for name in group_names:
    add_group(name)

# Commit changes to the database
session.commit()

# Close the session
session.close()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker object
fake = Faker()


# Function to add a professor to the database
def add_professor(name, degree):
    professor = Professor(name=name, degree=degree)
    session.add(professor)


# Add five professors
for _ in range(5):
    name = fake.name()
    degree = fake.random_element(elements=("Ph.D.", "M.Sc.", "D.Sc."))
    add_professor(name, degree)

# Commit changes to the database
session.commit()

# Close the session
session.close()

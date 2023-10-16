from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

import os
from dotenv import load_dotenv


# from itam.infrastructure.repository.sqlalchemy_asset_repository.SQLAlchemyAssetRepository import FundingDetailsModel, AssetModel, LocationModel  # Replace 'your_module' with the actual module where your models are defined
from itam.infrastructure.repository.sqlalchemy_asset_repository import SQLAlchemyAssetRepository

# Replace 'postgresql://username:password@localhost/dbname' with your PostgreSQL connection string
#engine = create_engine('postgresql://username:password@localhost/dbname')

def init_db():
    load_dotenv()
    engine = create_engine(f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}")

    # Create a session to inspect the models and generate SQL statements
    Base = declarative_base()
    Base.metadata.create_all(engine)
    print('tables create')

# # Optionally, you can create a session to interact with the database
# Session = sessionmaker(bind=engine)
# session = Session()

if __name__ == "__main__":
    init_db()

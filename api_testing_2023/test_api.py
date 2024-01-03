import pytest
from pytest import Session
from typing import Generator
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from main import DBItem, app, get_db, Base


# Setup the TestClient
client = TestClient(app)


# def setup():
#     # Create the tables in the test database
#     Base.metadata.create_all(bind=engine)

#     # create test items
#     session = TestingSessionLocal()
#     db_item = DBItem(id=1, name="Test Item", description="This is a test item")
#     session.add(db_item)
#     session.commit()
#     session.close()


# def teardown():
#     Base.metadata.drop_all(bind=engine)


# NOTE: using a pytest fixture
@pytest.fixture
def session() -> Generator[Session, None, None]:
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    # create test items
    db_item = DBItem(id=1, name="Test Item", description="This is a test item")
    session.add(db_item)
    session.commit()

    yield session

    # Close the db and drop the tables in the test database
    session.close()
    Base.metadata.drop_all(bind=engine)


# Setup the in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,  # for consistency in testing
    },
    poolclass=StaticPool,  # to reuse same instance of db
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to override the get_db dependency in the main app
def override_get_db():
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()


app.dependency_overrides[get_db] = override_get_db


def test_create_item(session: Session):
    response = client.post(
        "/items", json={"name": "Test Item", "description": "This is a test item"}
    )

    assert response.status_code == status.HTTP_200_OK, response.text
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert "id" in data


def test_update_item(session: Session):
    item_id = 1
    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated Item", "description": "This is an updated item"},
    )
    assert response.status_code == status.HTTP_200_OK, response.text
    data = response.json()
    assert data["name"] == "Updated Item"
    assert data["description"] == "This is an updated item"
    assert data["id"] == item_id


def test_delete_item(session: Session):
    item_id = 1
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == status.HTTP_200_OK, response.text
    data = response.json()
    assert data["id"] == item_id
    # Try to get the deleted item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text

import os

from app import add_numbers


def test_add_numbers():
  assert add_numbers(10, 7) == 17



def test_app_environment():
  assert os.environ["APP_ENV"] == "testing"

def test_demo_secret_exist():
  assert os.environ.get("DEMO_SECRET") is not None 

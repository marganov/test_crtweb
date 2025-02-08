import pytest
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def user_agent_data():
    file_path = Path(__file__).parent / "data" / "user_agent.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

@pytest.fixture(scope="module")
def browser(user_agent_data):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        # Создаем контекст с заголовком User-Agent
        context = browser.new_context(user_agent=user_agent_data["user_agent"])
        yield context
        context.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def office_info():
    file_path = Path(__file__).parent / "data" / "office_info.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

@pytest.fixture
def urls():
    file_path = Path(__file__).parent / "links" / "urls.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

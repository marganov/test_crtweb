import pytest
from playwright.sync_api import Page
from ..pages.main_page import MainPage
from ..pages.contacts_page import ContactsPage

def test_crtweb_contacts(page: Page, office_info, urls):
    # Открываем Яндекс
    page.goto(urls["search_engine"])

    # Вводим запрос и выполняем поиск
    page.fill('input[name="text"]', 'crtweb.ru')
    page.press('input[name="text"]', 'Enter')

    # Закрываем всплывающее окно
    page.get_by_role("button", name="Нет, спасибо").click()

    # Ожидание открытия новой страницы после клика
    with page.context.expect_page() as new_page_info:
        page.locator('span:has-text("ИТ аутсорсинг для бизнеса")').click()

    # Переходим к новой вкладке
    new_page = new_page_info.value
    new_page.wait_for_load_state()

    # Работаем с новой вкладкой
    main_page = MainPage(new_page)
    main_page.navigate_to_contacts()

    # Проверка информации на странице контактов
    contacts_page = ContactsPage(new_page)
    contacts_page.check_office_info(office_info)

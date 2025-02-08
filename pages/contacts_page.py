from .base_page import BasePage

class ContactsPage(BasePage):
    def check_office_info(self, office_info):
        errors = []  # Список ошибок для накопления отсутствующих элементов

        for label, expected_text in office_info.items():
            # Проверка наличия заголовка и текста
            if not self.page.locator(f"text={label}").is_visible():
                errors.append(f"Не найден элемент с текстом заголовка: '{label}'")
            if not self.page.locator(f"text={expected_text}").is_visible():
                errors.append(f"Не найден элемент с текстом значения: '{expected_text}'")

        # Если есть ошибки, выводим список всех недочетов
        if errors:
            error_message = "\n".join(errors)
            raise AssertionError(f"Ошибки на странице контактов:\n{error_message}")

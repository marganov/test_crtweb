from .base_page import BasePage

class MainPage(BasePage):
    def navigate_to_contacts(self):
        self.page.locator("#rec844101623").get_by_role("link", name="Контакты").click()
        
        
    '''
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="ИТ аутсорсинг для бизнеса -").click()
    page1 = page1_info.value
    page1.locator("#rec844101623").get_by_role("link", name="Контакты").click()
    '''   
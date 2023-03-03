import time
import pytest
import requests as r

from pom.elements_page import *


@pytest.mark.usefixtures('setup')  # split up in classes later
class TestElementsPage:
    # def test_text_box(self):
    #     text_box_page = TextBoxPage(self.driver)
    #     expected_output_forms_text = text_box_page.fill_all_fields()
    #     output_forms_text = text_box_page.get_output_forms_text()
    #     assert expected_output_forms_text == output_forms_text, 'Validating Elements page forms output text'
    #
    # def test_checkbox(self):
    #     checkbox = CheckBoxPage(self.driver)
    #     checkbox.expand_checkbox_list()
    #     checkbox.click_random_checkboxes()
    #     input_checkboxes = checkbox.get_checked_checkboxes_text()
    #     output_checkboxes = checkbox.get_output_results_text()
    #     print(input_checkboxes)
    #     print(output_checkboxes)
    #     assert input_checkboxes == output_checkboxes, 'Validating checked checkboxes in the hierarchy and output results'
    #
    # def test_radio_button(self):
    #     radio_button = RadioButtonPage(self.driver)
    #     expected_output = radio_button.get_active_rbs_text()
    #     actual_output = radio_button.get_output_after_rb_click()
    #     assert expected_output == actual_output
    #
    # def test_web_table(self):
    #     web_table = WebTablesPage(self.driver)
    #     submitted_person = web_table.submit_registration_form()
    #     table_entries = web_table.get_table_entries()
    #     print(submitted_person)
    #     print(type(submitted_person))
    #     print(table_entries)
    #     print(type(table_entries))
    #     print(type(submitted_person))
    #     assert submitted_person in table_entries, 'Validating submitted form to display correct in table'
    #
    # def test_web_table_search(self):
    #     web_table = WebTablesPage(self.driver)
    #     submitted_person = web_table.submit_registration_form()
    #     search_keyword = submitted_person[random.randint(0, 5)]
    #     web_table.fill_search_field(search_keyword)
    #     table_row = web_table.get_raw_text_by_delete_button()
    #     assert search_keyword in table_row, 'Validating that entering in search filed displays correct entry in the table'
    #
    # def test_rows_dropdown(self):
    #     web_table = WebTablesPage(self.driver)
    #     expected_rows_count = [5, 10, 20]
    #     rows_count = web_table.select_from_rows_dropdown()
    #     assert rows_count == expected_rows_count, 'Validating that selecting from rows dropdown changes the number of displayed rows in table'

    # def test_click_buttons(self):
    #     buttons_page = ButtonsPage(self.driver)
    #     buttons = buttons_page.BUTTONS
    #     success_click_text = buttons_page.SUCCESS_CLICK_TEXT
    #     for button in buttons:
    #         success = buttons_page.click_on_each_button(button)
    #         assert success in success_click_text, 'Validating if success text is present in expected success text list'

    # def test_home_link(self):
    #     links_page = LinksPage(self.driver)
    #     home_link_href, current_url = links_page.check_home_link()
    #     print(home_link_href, current_url)
    #     assert current_url == home_link_href, 'Validating that url of new tab matches href url'

    # def test_api_calls(self):
    #     links_page = LinksPage(self.driver)
    #     expected_status_message = links_page.get_api_call_links_text()
    #     response_code, response_message = links_page.check_api_call_links()
    #     expected_status_code = links_page.send_calls_get_status_code()
    #     for k, v in zip(expected_status_message, response_message):
    #         assert k in v, 'Validating that response message corresponds to link text '
    #     assert response_code == expected_status_code, 'Validating that status code corresponds to URL status code'

    def test_upload_download_page(self):
        upload_download_page = UploadDownloadPage(self.driver)
        # file_name, uploaded_file_name = upload_download_page.upload_file()
        # assert file_name == uploaded_file_name, 'Validating that uploaded filename matches result'
        check = upload_download_page.download_file()
        assert check is True, "Validating image download link"

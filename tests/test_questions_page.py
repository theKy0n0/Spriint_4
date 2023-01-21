import pytest
import allure
from pages.questions_page import QuestionsPage
from conftest import QUESTIONS_AND_ANSWERS


@allure.suite('Тест сьют для Q&A')
class TestQuestionPage:

    @allure.title('Открыть меню и проверить совпадение вопрос - ответ')
    @pytest.mark.parametrize('question, answer', QUESTIONS_AND_ANSWERS)
    def test_answer_matches_question_true(self, driver, question, answer):
        page = QuestionsPage(driver)
        page.accept_cookies()
        page.find_question(question)
        page.find_answer(answer)

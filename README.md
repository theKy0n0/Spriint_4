1. Установить зависимости из requirements.txt
```
pip3 install -r requirements.txt
```
2. Запустить тесты:
```
pytest tests --alluredir=allure_results
```
3. Открыть отчет Allure:
```
allure serve allure_results 
```

### Содержание:
```
README.md - этот файл
requirements.txt - основные зависимости
./conftest.py - конфигурация тестов
./tests/ - каталог с тестами
./tests/test_order_page.py - тесты для проверки создания заказа и навигации по логотипу
./tests/test_questions_page.py - тесты для проверки вопросов и ответов
./locators/ - каталог с локаторами
./locators/base_page_locators.py - локаторы на базовой странице
./locators/order_page_locators.py - локаторы для создания заказа
./locators/questions_page_locators.py - локаторы для проверки вопросов и ответов
./pages/ - каталог с классами страниц
./pages/base_page.py - класс для базовой страницы
./pages/order_page.py - класс для страницы оформления заказа
./pages/questions_page.py - класс для страницы с вопросами
./allure_results/ - каталог с Allure отчетом
```


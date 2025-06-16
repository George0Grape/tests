1. Установите необходимые зависимости:
   pip install pytest pytest-mock coverage httpx locust fastapi uvicorn

2. Запустите сервер FastAPI:
   uvicorn app.main:app --reload

3. Запустите тесты с покрытием:
   coverage run -m pytest tests/test_all.py

4. Посмотрите отчет о покрытии:
   coverage report -m
   или откройте HTML-отчет:
   coverage html
   и откройте htmlcov/index.html в браузере.
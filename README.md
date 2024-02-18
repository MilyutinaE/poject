- запуск из терминала: 
pytest
- в режиме headless: 
pytest --headless

(по умолчанию открывает опенкарт в хроме)
в edge браузере pytest --browser=edge
#options.add_argument('--enable-chrome-browser-cloud-management')  нужно, чтобы в терминале не было ошибк

- selenoid (нужно прописывать айпи, иначе тесты опенкарта будут падать)
pytest --remote=True --executor="172.18.240.1"



#pytest tests\test_main_page.py


#  AI-OSINT Recon Scanner

**AI-OSINT Recon Scanner** — это интеллектуальный сканер уязвимостей, который использует OSINT-фингерпринтинг и AI-анализ для выбора релевантных проверок безопасности.  
В отличие от классических сканеров, он не просто прогоняет базу CVE, а динамически подбирает тесты под стек конкретного сайта.

---

##  Возможности
- Сбор информации о цели (HTML, заголовки, favicon, title).
- AI-анализ собранных данных → рекомендации, какие уязвимости проверить.
- Поддержка базовых тестов: SQLi, XSS, слабые заголовки.
- CLI-интерфейс для запуска в терминале.

---

##  Структура проекта
```

ai-osint-recon-scanner/
│── cli/            # точка входа (CLI)
│── recon/          # сбор данных (collector, parser)
│── ai/             # анализ и генерация отчётов
│── scanner/        # проверки уязвимостей
│── utils/          # вспомогательные модули
│── webui/          # (опционально) веб-интерфейс

````

---

##  Установка
```bash
git clone https://github.com/<your-username>/ai-osint-recon-scanner.git
cd ai-osint-recon-scanner
pip install -r requirements.txt
````

---

## ▶ Запуск

Пример:

```bash
python -m cli.main --url https://example.com
```

Результат (JSON):

```json
{
    "url": "https://example.com",
    "status_code": 200,
    "title": "Example Domain",
    "favicon_hash": "abc123...",
    "headers": { ... }
}
```

AI-анализ:

```
[AI Analyzer] Recommended tests:
- Check for Path Traversal
- Check for SQL Injection
```

---

##  План развития

* [x] CLI и сбор данных
* [ ] Базовый AI-анализ (if-логика)
* [ ] Добавить первые тесты (SQLi, XSS, headers)
* [ ] Интеграция open-source LLM (Mistral 7B)
* [ ] Дообучение модели на CVE/Wappalyzer dataset
* [ ] Web-интерфейс для отчётов

---

##  Disclaimer

Этот проект создан в образовательных целях. Автор не несёт ответственности за использование инструмента против систем без разрешения.


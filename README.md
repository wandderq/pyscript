# PYScript

pyscript - это универсальный менеджер скриптов на Python, позволяющий легко создавать, запускать и управлять вашими скриптами


## Функции
- Позволяет быстро запускать ваши скрипты и управлять ими
- Предоставляет класс для создания скриптов


## Использование
- `pyscript run script-name` - запускает скрипт по имени
- `pyscript list` - показывает все доступные скрипты
- `pyscript add /path/to/script` - проверяет и перемещает ваш скрипт ко всем остальным
- `pyscript -V` - показываект версию pyscript и путь к директории скриптов


## Установка
1. Через pip (быстрее всего)
    ```bash
    pip install git+https://github.com/wandderq/pyscript
    pyscript -V
    ```

2. Вручную (если хотите модифицировать)
    ```bash
    git clone https://github.com/wandderq/pyscript
    cd pyscript
    ```
    так же, по желанию можете создать venv:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```


## Примеры
Вы можете найти примеры скриптов в [папке](https://github.com/wandderq/pyscript/tree/main/scripts) со скриптами

## Лицензия
Этот проект использует [лицензию MIT](LICENSE)

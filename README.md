# PYScript

pyscript - это универсальный менеджер скриптов на Python, позволяющий легко создавать, запускать и управлять вашими скриптами

## Функции
- Позволяет быстро запускать ваши скрипты и управлять ими
- Предоставляет класс для создания скриптов

## Использование
```
usage: pyscript [-h] [-v] [-V]  ...

Universal scripts launcher and manager

positional arguments:
  
    run          Run PYScript script
    list         Show all available scripts

options:
  -h, --help     show this help message and exit
  -v, --verbose  Verbose mode (debug logs)
  -V, --version  Get pyscript version and some other stuff
```

- `pyscript run script-name` - запускает скрипт по имени
- `pyscript list` - показывает все доступные скрипты
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

## Лицензия
Этот проект использует [лицензию MIT](LICENSE)

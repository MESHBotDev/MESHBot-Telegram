# MESHBot-Telegram
Телеграм бот решающий задания ЦДЗ.

# Описание:
[Бот](https://github.com/superdima05/mesh) написан с использованием библиотеки [`libmesh`](http://t.me/CDZMESHBot).
Для начала работы отправьте ему ссылку на тест и он попробует найти на него ответы.

# Запуск:
##### 1. Получите токен Вашего бота через @BotFather.
##### 2. Измените значение ключа `"telegram_token"` из файла `./src/package/client.json` на Ваш токен.
```py
{
    "telegram_token": "{token}"
}
```
##### 3. Запустите ./src/main.py.

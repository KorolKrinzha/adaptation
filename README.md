# Сайт для Адаптации | Лицей НИУ ВШЭ

## Описание

Проект является доработкой моей прошлой [работы](https://github.com/KorolKrinzha/SELFLYC).

Сайт предназначен для только что поступивших лицеистов. Во время первых месяцев обучения ученикам предстоит выполнить различные активности, направленные на знакомство с лицейской жизнью. Мой сайт поможет мотивировать лицеистов проходить этапы адаптации. За выполнение активностей пользователи получают баллы, которые могут использованы в Лицее

## Нововведения

Администраторы смогут просматривать информацию о пользователях (количество баллов, пройденные испытания) и самостоятельно создавать события и QR-коды к ним

## Технические детали

Фронтенд: React, Bootstrap

Бэкенд: Flask

БД: MySQL

## Этапы работы

Здесь я буду публиковать короткие отчеты о проделанной работе

**07.07.2022** Получил предложение сделать сайт. Продумал улучшения и определился с технологическим стеком

**08.07.2022** Создал шаблонный проект, совмещающий работу сервера (бэкенд) и отображение работы в браузере (фронтэнд). Работал над фронтэндом, создавал шаблоны, которые в будущем пригодятся для создания страниц. Сделал страницы с верификацией пользователей

**09.07.2022** Начал работу над БД и бэком. Сделал черновую регистрацию и логин.

! Надо доработать проверку и обработку ошибок форм регистрации и логина

Завтра буду делать динамичные ивенты

**10.07.2022** Работа над таблицами ивентов. Теперь за уникальное посещение пользователю начисляются баллы

**11.07.2022** Сделал функционал личного кабинета. Теперь в нем пользователь может видеть свои баллы, никнейм и все посещенные им ивенты

**12.07.2022** Работа над скорбордом

**15.07.2022** Скорборд функционально доделан, остался только экспорт pdf. Сделана страница админов с ивентами, там можно редактировать (а скоро и удалять) мероприятия

**16.07.2022** Обезопасил работу с БД. Добавлена работа динамичных ивентов

**17.07.2022** Добавил необходимость аутентификации для посещения личного кабинета и ивентов. Админ-страницы теперь недоступны обычным пользователям

**20.07.2022** API-запросы админов и пользователей защищены. Добвлены логи посещений ивентов для админов. Практически полностью доделана обработка ошибок, осталось доделать страницы Sign/Login

**21.07.2022** QR-коды ивентов теперь можно скачивать как архивом, так и единичными файлами

**22.07.2022** QR-коды теперь обновляются корректна, выбраны цвета и шрифты для сайта

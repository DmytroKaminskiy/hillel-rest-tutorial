# hillel-rest-tutorial

## Данный проект предназначен для обучения студентов компьютерной школы Hillel.

### Цель:
 - использовать REST API, 
 - понимать клиент-серверную архитектуру, 
 - освоить цикл "запрос-ответ"
 - изучить базовую структуру HTTP запроса-ответа
 
## /hello-world/
GET return {"data": "Hello, world!"}

## /status/
GET return Список возможных статусов ответов

##/status/{hhtp_status_number}
GET return Возвращает данный статус с описанием

## /get-my-ip/
GET Возвращает IP пользователя

## /text/
POST json {"text": {text}}

GET Возвращает {text} пользователя

# Модель - авторы книг
### Описание модели данных

- ID
- FirstName
- LastName
- DateOfBirth
- DateOfDeath
- Email
- Country
- Gender
- Language
- _created_by_student (date time)

## Endpoints
### /authors/
GET
- Список авторов (все поля)
- Должна присутствовать пагинация
- Фиьтры по полям

POST
- Создать автора
### /authors/id/
GET
- Детальная информация по автору (все поля + книги автора)

PUT
- Обновить заданные поля
DELETE
- Удалить при условии _created_by_student не Null


# Модель - книги
### Описание модели данных

- ID
- Title
- PublishYear
- AuthorId
- _created_by_student (date time)





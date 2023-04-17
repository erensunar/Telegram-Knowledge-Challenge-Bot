# Knowledge Challenge Bot

Knowledge Challenge Bot, Telegram üzerinden kullanıcılara soru-cevap oyunu oynatmak için tasarlanmış bir bot uygulamasıdır. Kullanıcılar, bot ile etkileşime geçerek rastgele seçilen sorulara doğru cevaplar vermeye çalışırlar ve puan kazanırlar. Kazandıkları puan ile liderlik tablosunda ilerleyebilir ve bu tabloyu görüntüleyebilir. Belli bir puana erişmiş kullanıcılar soru önerisinde bulunur ve onaylanan sorular yarışmalarda kullanılır.

## Getting Started

### Firebase Realtime Database Docs

#### Users

- id: the user's identification information (string)
- first_name: the user's first name (string)
- last_name: the user's last name (string)
- chat_id: the user's Telegram chat ID (string)
- remaining_attempts: the number of remaining attempts for the user (integer)
- score: the user's total score (integer)
- answered_questions: IDs of the questions answered by the user (list of strings)

#### Questions

- id: the question's identification information (string)
- text: the question's text (string)
- category: the question's category (string)
- author: the question's author (string)
- answers: an array that contains the answers (string)
- correct_answer: the text of the correct answer (string)

#### Suggestion

- id: suggestion ID (string)
- user_id: ID of the user who made the suggestion (string)
- name: name of the user who made the suggestion (string)
- text: suggestion text (string)
- category: suggestion category (string)
- status: suggestion status (string, "new", "approved", "rejected")


## API Documentation

### Create User
- **Endpoint:** `/create_user`
- **Method:** `POST`
- **Description:** Creates a new user with the provided Telegram user information and adds them to the database.
- **Request Body:**

```bash
    {
    "telegram_id": "1234567890",
    "first_name": "John",
    "last_name": "Doe",
    "chat_id": "-1234567890"
    }
```

- `telegram_id` (string, required): The Telegram ID of the user.
- `first_name` (string, required): The first name of the user.
- `last_name` (string, required): The last name of the user.
- `chat_id` (string, required): The chat ID of the user.

- **Response Body:**

```bash
    {
    "message": "User created successfully!"
    }
```

- **Example:**

```bash
    curl -X POST -H "Content-Type: application/json" -d '{"telegram_id": "1234567890", "first_name": "John", "last_name": "Doe", "chat_id": "-1234567890"}' http://localhost:5000/create_user
```

### Check User

- **Endpoint:** `/check_user/<telegram_id>`
- **Method:** `GET`
- **Description:** Checks if the user with the provided Telegram ID exists in the database.
- **Parameters:**

    - `telegram_id` (string, required): The Telegram ID of the user.

- **Response Body:**

```json
{
    "message": "User exists",
    "exists": true
}
```
or

```json
{
    "message": "User does not exist",
    "exists": false
    }
```
- **Example:**

```bash
    curl -X GET http://localhost:5000/check_user/1234567890

```

### Leaderboard

- **Endpoint:** `/leaderboard`
- **Method:** `GET`
- **Description:** Returns the top 10 users with the highest scores.

- **Response Body:**

```json
{
    "leaderboard": [
        {
            "name": "John Doe",
            "score": 1000
        },
        {
            "name": "Jane Doe",
            "score": 950
        },
        ...
    ]
}

```
- **Example:**

```bash
    curl -X GET http://localhost:5000/leaderboard
```

### Score Add

- **Endpoint:** `/score/add/<telegram_id>`
- **Method:** `PUT`
- **Description:** Adds 10 points to the user with the given Telegram ID and returns the updated score.

- **Response Body:**

```json
{
    "message": "<telegram_id>'s score has been increased by 10",
    "success": true,
    "score": 50
}

```
- **Example:**

```bash
    curl -X PUT http://localhost:5000/score/add/1234567890
```

### Score Add

- **Endpoint:** `/score/subtract/<telegram_id>`
- **Method:** `PUT`
- **Description:** Subtracts 5 points from the user with the given Telegram ID and returns the updated score.

- **Response Body:**

```json
{
    "message": "<telegram_id>'s score has been subtracted by 5",
    "success": true,
    "score": 35
}

```
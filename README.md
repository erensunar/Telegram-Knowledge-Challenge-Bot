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


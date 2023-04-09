# Knowledge Challenge Bot

Knowledge Challenge Bot, Telegram üzerinden kullanıcılara soru-cevap oyunu oynatmak için tasarlanmış bir bot uygulamasıdır. Kullanıcılar, bot ile etkileşime geçerek rastgele seçilen sorulara doğru cevaplar vermeye çalışırlar ve puan kazanırlar. Kazandıkları puan ile liderlik tablosunda ilerleyebilir ve bu tabloyu görüntüleyebilir. Belli bir puana erişmiş kullanıcılar soru önerisinde bulunur ve onaylanan sorular yarışmalarda kullanılır.

## Getting Started

### Firebase Realtime Database Docs

#### Users

[TR]
- id: kullanıcının kimlik bilgisi (string)
- first_name: kullanıcının adı (string)
- last_name: kullanıcının soyadı (string)
- chat_id: kullanıcının Telegram chat ID'si (string)
- remaining_attempts: kullanıcının kalan deneme hakkı sayısı (integer)
- score: kullanıcının toplam puanı (integer)
- answered_questions: kullanıcının cevapladığı soruların ID'leri (list of strings)

[EN]
- id: the user's identification information (string)
- first_name: the user's first name (string)
- last_name: the user's last name (string)
- chat_id: the user's Telegram chat ID (string)
- remaining_attempts: the number of remaining attempts for the user (integer)
- score: the user's total score (integer)
- answered_questions: IDs of the questions answered by the user (list of strings)

#### Questions

[TR]
- id: sorunun kimlik bilgisi (string)
- text: sorunun metni (string)
- category: sorunun kategorisi (string)
- answers: sorunun cevapları  (array)
- answer_1: cevap 1'in metni (string)
- answer_2: cevap 2'nin metni (string)
- answer_3: cevap 3'ün metni (string)
- answer_4: cevap 4'ün metni (string)
- correct_answer: Doğru cevap metni (string)

[EN]
- id: the question's identification information (string)
- text: the question's text (string)
- category: the question's category (string)
- answers: a dictionary that contains the answers and which one is correct (boolean)
- answer_1: the text of answer 1 (string)
- answer_2: the text of answer 2 (string)
- answer_3: the text of answer 3 (string)
- answer_4: the text of answer 4 (string)
- correct_answer: the text of the correct answer (string)


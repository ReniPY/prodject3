import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

website = 'https://dvmn.org/profession-ref-program/denos2/DXkai/'
riend_name = 'Ваня'
my_name = 'Данил'
message = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace('%website%', website).replace('%friend_name%', riend_name).replace('%my_name%', my_name)

email_from = 'denos00@yandex.ru'
email_to = 'daf.caf@yandex.ru'
subject = 'Приглашение!'
letter = '''From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";

{3} '''.format(email_from, email_to, subject, message)

letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()
## Тестовое задание python backend developer

Нужно спроектировать реляционную базу данных и написать API-сервис для управления вебинарами и курсами
Framework на выбор: Django или FastAPI
В качестве БД можно использовать PostgreSQL.
В сервисе должно быть реализовано создание, изменение, удаление, получение вебинаров и курсов.
Обязательные модели: Вебинар, Курс, Преподаватель
Вебинар должен иметь несколько статусов: Создан, сейчас идет, закончен, отменен
У вебинара может быть несколько преподавателей
 
Доп. задание:
Реализовать логику подсчета зарплат преподавателей и API для получения зарплат. Преподаватель имеет свою часовую ставку на каждый свой курс.




<p align="center">
     <a href="https://ibb.co/s1c0hzr"><img src="https://i.ibb.co/SmHh2Gp/63472c251357681c4637a6f0-thanfoxy.png" alt="63472c251357681c4637a6f0-thanfoxy" border="0"></a>
</p>


<p align="center">
   <img src="https://img.shields.io/badge/django-4.1.6-blueviolet" alt="django Version" >
   <img src="https://img.shields.io/badge/DRF-3.14.0-blue" alt="DRF Version">
   <img src="https://img.shields.io/badge/PostgreSQL-14-orange" alt="PostgreSQL Version">
   <img src="https://img.shields.io/badge/LICENSE-MIT-brightgreen" alt="License">
</p>

## Документация


Прописать свои параметры PostgreSQL в DATABASES

<pre>
<span class="key">/foxford_api/settings.py</span>
</pre>



Example Request swagger documentation.

<pre>
<span class="key">http://127.0.0.1:8000/swagger/</span>
</pre>

<p align="left">
     <a href="https://ibb.co/DpNVv3T"><img src="https://i.ibb.co/hfk74pw/K73ySNnJ.jpg" alt="K73ySNnJ" border="0"></a>
</p>


## Дополнительные параметры

  Для каждого учителя реализовано поле выбора курсов, которые он ведет

  Регистрация учеников
  
  Выбор курса для вебинара
  
  Выбор времени начала вебинара
  
  Выбор языка вебинара
  
  Выбор и добавление учеников к вебинару


<p align="left">
     <a href="https://ibb.co/mNBwhmv"><img src="https://i.ibb.co/DrbywNG/hhOAXIBP.jpg" alt="hhOAXIBP" border="0"></a>
</p>


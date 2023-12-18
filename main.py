# #LAB (общ)
#
# import sqlite3
# # создаем базу данных и устанавливаем соединение с ней
# con = sqlite3.connect("library.sqlite")
# # открываем файл с дампом базой двнных
# f_damp = open('booking.db','r', encoding ='utf-8-sig')
# # читаем данные из файла
# damp = f_damp.read()
# # закрываем файл с дампом
# f_damp.close()
# # запускаем запросы
# con.executescript(damp)
# # сохраняем информацию в базе данных
# con.commit()
# # создаем курсор
# cursor = con.cursor()
# # выбираем и выводим записи из таблиц author, reader
# cursor.execute("SELECT * FROM room")
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM room_booking")
# print(cursor.fetchall())
# # закрываем соединение с базой
# con.close()


# #LAB (1)
#
#
# import sqlite3
#
# # создаем базу данных и устанавливаем соединение с ней
# con = sqlite3.connect("library.sqlite")
#
# # открываем файл с дампом базой двнных
# with open('booking.db', 'r', encoding='utf-8-sig') as f_damp:
#     # читаем данные из файла
#     damp = f_damp.read()
#     # запускаем запросы
#     con.executescript(damp)
#     # сохраняем информацию в базе данных
#     con.commit()
#
# # создаем курсор
# cursor = con.cursor()
#
# # Ваш SQL-запрос
# query = """
# SELECT
#     r.room_name AS "Название номера",
#     b.check_in_date AS "Дата заселения",
#     b.check_out_date AS "Дата выселения",
#     julianday(b.check_out_date) - julianday(b.check_in_date) + 1 AS "Дни",
#     (julianday(b.check_out_date) - julianday(b.check_in_date) + 1) * t.price AS "Счет"
# FROM
#     room r
# JOIN
#     room_booking b ON r.room_id = b.room_id
# JOIN
#     type_room t ON r.type_room_id = t.type_room_id
# WHERE
#     t.type_room_name = 'Стандартный двухместный номер'
#     AND b.status_id = (SELECT status_id FROM status WHERE status_name = 'Занят')
# ORDER BY
#     r.room_name ASC,
#     "Счет" DESC,
#     b.check_in_date DESC;
# """
#
# cursor.execute(query)
#
# # Вывод результатов
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# # закрываем соединение с базой
# con.close()


# # LAB (2)
#
# import sqlite3
#
# # создаем базу данных и устанавливаем соединение с ней
# con = sqlite3.connect("library.sqlite")
#
# # открываем файл с дампом базой двнных
# with open('booking.db', 'r', encoding='utf-8-sig') as f_damp:
#     # читаем данные из файла
#     damp = f_damp.read()
#     # запускаем запросы
#     con.executescript(damp)
#     # сохраняем информацию в базе данных
#     con.commit()
#
# # создаем курсор
# cursor = con.cursor()
#
# # Ваш SQL-запрос
# query = """
# SELECT
#     s.service_name AS "Услуга",
#     COALESCE(COUNT(sb.service_id), '-') AS "Количество",
#     COALESCE(ROUND(AVG(sb.price), 2), '-') AS "Средняя_цена",
#     COALESCE(SUM(sb.price), '-') AS "Сумма"
# FROM
#     service s
# LEFT JOIN
#     service_booking sb ON s.service_id = sb.service_id
# GROUP BY
#     s.service_name
# ORDER BY
#     CASE WHEN "Сумма" = '-' THEN 1 ELSE 0 END,
#     "Сумма" DESC,
#     "Услуга" ASC;
# """
#
# cursor.execute(query)
#
# # Вывод результатов
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# # закрываем соединение с базой
# con.close()


# # LAB (3)
#
# import sqlite3
#
# # создаем базу данных и устанавливаем соединение с ней
# con = sqlite3.connect("library.sqlite")
#
# # открываем файл с дампом базой двнных
# with open('booking.db', 'r', encoding='utf-8-sig') as f_damp:
#     # читаем данные из файла
#     damp = f_damp.read()
#     # запускаем запросы
#     con.executescript(damp)
#     # сохраняем информацию в базе данных
#     con.commit()
#
# # создаем курсор
# cursor = con.cursor()
#
# # Ваш SQL-запрос
# query = """
# WITH GuestFrequency AS (
#     SELECT
#         guest_id,
#         COUNT(*) as count
#     FROM
#         room_booking
#     GROUP BY
#         guest_id
#     ORDER BY
#         count DESC
#     LIMIT 1
# )
#
# SELECT
#     g.guest_name AS "Номер",
#     gf.count AS "Количество",
#     GROUP_CONCAT(tr.type_room_name, ', ') AS "Типы_номеров"
# FROM
#     GuestFrequency gf
# JOIN
#     guest g ON gf.guest_id = g.guest_id
# JOIN
#     room_booking rb ON gf.guest_id = rb.guest_id
# JOIN
#     room r ON rb.room_id = r.room_id
# JOIN
#     type_room tr ON r.type_room_id = tr.type_room_id
# GROUP BY
#     g.guest_name
# ORDER BY
#     g.guest_name ASC;
# """
#
# cursor.execute(query)
#
# # Вывод результатов
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# # закрываем соединение с базой
# con.close()


# LAB (4)


# import sqlite3
#
# # создаем базу данных и устанавливаем соединение с ней
# con = sqlite3.connect("library.sqlite")
#
# # открываем файл с дампом базой данных
# with open('booking.db', 'r', encoding='utf-8-sig') as f_damp:
#     # читаем данные из файла
#     damp = f_damp.read()
#     # запускаем запросы
#     con.executescript(damp)
#     # сохраняем информацию в базе данных
#     con.commit()
#
# # создаем курсор
# cursor = con.cursor()
#
# # Создание таблицы bill
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS bill (
#     Вид_платежа TEXT,
#     Сумма REAL
# );
# """)
#
# # Добавление стоимости проживания
# cursor.execute("""
# INSERT INTO bill
# WITH RoomCost AS (
#     SELECT
#         tr.type_room_name || ' ' || r.room_name || ' ' || rb.check_in_date || '/' || DATE('now') AS "Вид_платежа",
#         (julianday(DATE('now')) - julianday(rb.check_in_date) + 1) * tr.price AS "Сумма"
#     FROM
#         room_booking rb
#     JOIN
#         guest g ON rb.guest_id = g.guest_id
#     JOIN
#         room r ON rb.room_id = r.room_id
#     JOIN
#         type_room tr ON r.type_room_id = tr.type_room_id
#     WHERE
#         g.guest_name = 'Садиев С.И.' AND r.room_name = 'С-0226' AND rb.check_in_date = '2020-11-04'
# )
# SELECT * FROM RoomCost;
# """)
#
# # Добавление стоимости услуг
# cursor.execute("""
# INSERT INTO bill
# WITH ServicesCost AS (
#     SELECT
#         s.service_name || ' ' || sb.service_start_date AS "Вид_платежа",
#         SUM(sb.price) AS "Сумма"
#     FROM
#         service_booking sb
#     JOIN
#         service s ON sb.service_id = s.service_id
#     WHERE
#         sb.room_booking_id = (SELECT rb.room_booking_id FROM room_booking rb JOIN guest g ON rb.guest_id = g.guest_id WHERE g.guest_name = 'Садиев С.И.' AND rb.check_in_date = '2020-11-04')
#     GROUP BY
#         s.service_name, sb.service_start_date
# )
# SELECT * FROM ServicesCost;
# """)
#
# # Добавление строки "Итого"
# cursor.execute("""
# INSERT INTO bill
# SELECT 'Итого', SUM(Сумма) FROM bill;
# """)
#
# # Вывод результатов
# cursor.execute("SELECT * FROM bill;")
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# # закрываем соединение с базой
# con.close()

# # LAB (5)
#
# import sqlite3
#
# # создаем базу данных и устанавливаем соединение с ней
# con = sqlite3.connect("library.sqlite")
#
# # открываем файл с дампом базой данных
# with open('booking.db', 'r', encoding='utf-8-sig') as f_damp:
#     # читаем данные из файла
#     damp = f_damp.read()
#     # запускаем запросы
#     con.executescript(damp)
#     # сохраняем информацию в базе данных
#     con.commit()
#
# # создаем курсор
# cursor = con.cursor()
#
# # Ваш SQL-запрос
# query = """
# WITH MonthlyServiceCount AS (
#     SELECT
#         strftime('%Y', sb.service_start_date) AS "Год",
#         strftime('%m', sb.service_start_date) AS "Месяц",
#         s.service_name AS "Услуга",
#         COUNT(*) AS service_count,
#         AVG(sb.price) AS avg_price,
#         ROW_NUMBER() OVER(
#             PARTITION BY strftime('%Y', sb.service_start_date), strftime('%m', sb.service_start_date)
#             ORDER BY COUNT(*) DESC, AVG(sb.price) DESC
#         ) AS rn
#     FROM
#         service_booking sb
#     JOIN
#         service s ON sb.service_id = s.service_id
#     WHERE
#         strftime('%Y', sb.service_start_date) IN ('2020', '2021')
#     GROUP BY
#         strftime('%Y', sb.service_start_date), strftime('%m', sb.service_start_date), s.service_name
# )
#
# SELECT
#     Год, Месяц, Услуга
# FROM
#     MonthlyServiceCount
# WHERE
#     rn = 1
# ORDER BY
#     Год ASC, Месяц ASC;
# """
#
# cursor.execute(query)
#
# # Вывод результатов
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# # закрываем соединение с базой
# con.close()

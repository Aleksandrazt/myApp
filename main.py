import sys
import time

import pandas as pd
import sqlite3
import generation

DB_CONFIG = {'database': 'myAppDB'}
QUERIES = {'1': 'CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,full_name VARCHAR(100),birth_date DATE, '
                'gender VARCHAR(1));',
           '3': "SELECT full_name, birth_date, gender, ROUND((julianday('now') - julianday(birth_date))/365.25) "
                "FROM users GROUP BY full_name, birth_date ORDER BY full_name;",
           '5': "SELECT * FROM users WHERE gender = 'm' AND full_name LIKE 'F%';",
           '6': 'SELECT * FROM users;',
           '7': 'DROP TABLE users;',
           '8': 'SELECT COUNT(id) FROM users;',
           '9': 'CREATE INDEX index_gender ON users(gender);'}


def send_query_to_db(query):
    print(query)
    cnx = sqlite3.connect(**DB_CONFIG)
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    result = cursor.fetchall()
    cnx.close()
    if result:
        result = pd.DataFrame(result)
        pd.options.display.expand_frame_repr = False
    else:
        result = 'Done'
    return result


def main():
    if sys.argv[1] == '2':
        try:
            query = f"INSERT INTO users (full_name, birth_date, gender) " \
                    f"VALUES ('{sys.argv[2]} {sys.argv[3]} {sys.argv[4]}', '{sys.argv[5]}', '{sys.argv[6]}');"
        except IndexError:
            print('Not enough info')
        else:
            result = send_query_to_db(query)
            print(result)
    elif sys.argv[1] == '4':
        for _ in range(1000000):
            surname, name, father_name, date, gen = generation.generate_users().__next__()
            query = f"INSERT INTO users (full_name, birth_date, gender) " \
                    f"VALUES ('{surname} {name} {father_name}', '{date}', '{gen}');"
            send_query_to_db(query)
        for _ in range(100):
            surname, name, father_name, date = generation.generate_users_with_f().__next__()
            query = f"INSERT INTO users (full_name, birth_date, gender) " \
                    f"VALUES ('{surname} {name} {father_name}', '{date}', 'm');"
            send_query_to_db(query)
    else:
        try:
            result = send_query_to_db(QUERIES[sys.argv[1]])
        except KeyError:
            print('Unknown Command')
        else:
            print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time()-start)

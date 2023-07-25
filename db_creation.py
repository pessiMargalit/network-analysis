from db_connection import connect_to_db

connection = connect_to_db()


def create_table(query):
    try:
        with connection.cursor() as cursor:
            # query = "CREATE TABLE client (id INT NOT NULL AUTO_INCREMENT,  name VARCHAR(255) NOT NULL,   PRIMARY KEY (id) )"
            cursor.execute(query)
            # cursor.execute("SHOW TABLES")
            connection.commit()
    except:
        print("DB Error")


def insert_to_table(query):
    try:
        with connection.cursor() as cursor:
            # query = 'INSERT into client (name) values ("Wix")'
            cursor.execute(query)
            connection.commit()
    except:
        print("Error")


def get_all_from_table(table_name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


if __name__ == '__main__':
    query = r"CREATE TABLE network (id INT NOT NULL AUTO_INCREMENT, client_id INT NOT NULL," \
            " premises VARCHAR(255) NOT NULL, date DATE NOT NULL, " \
            "PRIMARY KEY (id), FOREIGN KEY (client_id) REFERENCES client(id))"
    # query = r"CREATE TABLE technician (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL,  PRIMARY KEY (id) )"
    # query = r"CREATE TABLE device (id INT NOT NULL AUTO_INCREMENT, MAC_address VARCHAR(255) NOT NULL," \
    #         r" vendor VARCHAR(255) NOT NULL,network_id INT NOT NULL, PRIMARY KEY (id), " \
    #         r" FOREIGN KEY (network_id) REFERENCES network(id))"
    # query = r"CREATE TABLE technician_clients (technician_id INT NOT NULL," \
    #         r" client_id INT NOT NULL, " \
    #         r" FOREIGN KEY (technician_id) REFERENCES technician(id)," \
    #         r" FOREIGN KEY (client_id) REFERENCES client(id))"
    # query = r"CREATE TABLE device_connection (network_id INT NOT NULL," \
    #         r" source INT NOT NULL, " \
    #         r" destination INT NOT NULL, " \
    #         r" protocol VARCHAR(255) NOT NULL, " \
    #         r" FOREIGN KEY (network_id) REFERENCES network(id)," \
    #         r" FOREIGN KEY (source) REFERENCES device(id)," \
    #         r" FOREIGN KEY (destination) REFERENCES device(id))"

    # create_table(query)

    # query_to_insert = "INSERT INTO network (client_id, premises, date) values (1,'Tel Aviv', '2020-03-07')"
    # query_to_insert = 'INSERT into technician (name) values ("Dan")'
    # query_to_insert = "INSERT INTO device (MAC_address, vendor, network_id) values ('84-A9-3E-AE-80-9B'," \
    #                   " 'Hewlett Packard', 1)"
    # query_to_insert = "INSERT INTO technician_clients (technician_id, client_id) values (1, 1)"
    #query_to_insert = "INSERT INTO device_connection (network_id, source, destination, protocol) values (1, 1, 2, 'UDP')"
    # query_to_update = "UPDATE technician SET email = 'dantech@gmail.com' ,password = 'passwors1234' WHERE id = 1"
    # query_to_update = "ALTER TABLE technician ADD COLUMN email VARCHAR(255) AFTER name,ADD COLUMN password VARCHAR(255) AFTER email"
    query_to_change = "ALTER TABLE technician CHANGE password password VARCHAR(255) NOT NULL"
    insert_to_table(query_to_change)

    get_all_from_table("technician")

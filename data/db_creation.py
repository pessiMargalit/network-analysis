from db_connection_server import connect_to_db

connection = connect_to_db()


def create_table(query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            # cursor.execute("SHOW TABLES")
            connection.commit()
    except:
        print("DB Error")


def insert_to_table(query):
    try:
        with connection.cursor() as cursor:
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
    pass
    # query = "CREATE TABLE client (id INT NOT NULL AUTO_INCREMENT,  name VARCHAR(255) NOT NULL,   PRIMARY KEY (id) )"
    # query = r"CREATE TABLE network (id INT NOT NULL AUTO_INCREMENT, client_id INT NOT NULL," \
    #         " premises VARCHAR(255) NOT NULL, date DATE NOT NULL, " \
    #         "PRIMARY KEY (id), FOREIGN KEY (client_id) REFERENCES client(id))"
    # query = r"CREATE TABLE technician (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, PRIMARY KEY (id) )"
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
    #
    # create_table(query)

    # query_to_insert = 'INSERT into client (name) values ("Wix")'
    # query_to_insert = "INSERT INTO network (client_id, premises, date) values (1,'Jerusalem', '2021-07-07')"
    # query_to_insert = 'INSERT into technician (name, email, password) values ("Dan", "dantech@gmail.com", "password1234")'
    # query_to_insert = "INSERT INTO device (MAC_address, vendor, network_id) values ('00:1b:63:84:45:e6'," \
    #                   " 'Apple, Inc.', 2)"
    # query_to_insert = "INSERT INTO technician_clients (technician_id, client_id) values (1, 1)"
    # query_to_insert = "INSERT INTO device_connection (network_id, source, destination, protocol) values (2, 3, 4, 'TCP')"
    # query_to_delete = "DELETE FROM client WHERE id = 2"
    # query_to_update = "UPDATE network SET MAC_address = 'd0-c5-d3-b0-3b-c1' WHERE id = 3"

    # insert_to_table(query_to_insert)
    # get_all_from_table("")

import configparser

# creating object of configparser
config = configparser.ConfigParser()

config.add_section("database")

config.set("database", "user", "root")
config.set("database", "password", "")
config.set("database", "database", "network_analysis")

with open("../data/db_config.ini", 'w') as conf:
    config.write(conf)
























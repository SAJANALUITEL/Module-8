import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2011',
    autocomit=True
)

def get_airport_by_ident(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if result:
        name, location = result
        print(f"Airport Name: {name}")
        print(f"Location: {location}")
    else:
        print(f"No airport found with ICAO code: {icao}")

if __name__ == "__main__":
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    get_airport_by_ident(icao_code)

    connection.close()
    
import requests
import psycopg2

def Functionurl(url):
    resp = requests.get(url)
    if resp.status_code == 404: 
      return "Error 404"
    return resp.json()

def get_database_connection(): 
    try: 
        conn = psycopg2.connect( 
          dbname="nueva_data", 
          user="postgres", 
          password="a", 
          host="localhost", 
          port="5432" 
          ) 
        return conn 
    except Exception as e: 
        print(f"Error al conectar a la base de datos: {e}") 
        return None 
    
conecction=get_database_connection()
cursor = conecction.cursor()
    
def fetch_user_by_id(user_id): 
    conn = get_database_connection() 
    if conn is None: 
        return None 
    try: 
        cur = conn.cursor() 
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,)) 
        user = cur.fetchone() 
        conn.close() 
        return user 
    except Exception as e: print(f"Error al ejecutar la consulta: {e}") 
    return None

# Insertar datos
insert_query = "INSERT INTO users (name, age) VALUES ('Carla', 28), ('Meyling', 30)"

cursor.execute(insert_query)
conecction.commit()

#Consultar datos
select_query = "SELECT * FROM users;"
cursor.execute(select_query)
records = cursor.fetchall()
for record in records:
 print(record)

############################################
def delete_user_by_name(name):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        delete_query = "DELETE FROM users WHERE name = %s"
        cursor.execute(delete_query, (name,))
        connection.commit()
        print(f"Registro(s) de '{name}' eliminado(s) exitosamente")

        cursor.close()
        connection.close()

    except Exception as error:
        print(f"Error al eliminar datos: {error}")

# Ejemplo de uso
delete_user_by_name("Eliany")
###########################################

def mock_get_database_connection():
    class MockConnection:
        def cursor(self):
            class MockCursor:
                def execute(self, query, params=None):
                    pass
                def fetchone(self):
                    return (1, "Alice")
            return MockCursor()
        def close(self):
            pass
    return MockConnection()

# Llama a la función para ejecutar las consultas
get_database_connection()


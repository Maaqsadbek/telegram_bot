
import sqlite3

class Database:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db=path_to_db

    @property
    def connection(self):
            return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone= False, fetchall=False, commit=False):
        if not parameters:
            parameters=()
        connection=self.connection
        connection.set_trace_callback(logger)
        cursor=connection.cursor()
        data=None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data=cursor.fetchall()
        if fetchone:
            data=cursor.fetchone()
        connection.close()
        return data
    def create_table_users(self):
        sql="""
        CREATE TABLE Users(
            id int not NULL,
            Name varchar(255) not NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY(id)
            ); 
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql+="AND".join([
            f"{item}=?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    def add_user(self, id: int, name: str, email: str=None, language: str='uz'):
        #SQL_EXAMPLE="INSERT INTO User(id, name,email) Values(1,'john','john@gmail.com')"
        sql="""
        INSERT INTO Users(id, name, email,language) Values(?,?,?,?)
        """
        self.execute(sql, parameters = (id,name,email,language), commit=True)
    def select_all_users(self, **kwargs):
        sql="""
        SELECT * FROM Users
        """
        sql, parameters=self.format_args(sql, kwargs)
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        #SQL EXAMPLE ="select * from users where id=1 AND name='john'"
        sql="SELECT * FROM Users WHERE"
        sql, parameters=self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT (*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL EXAMPLE="UPDATE Users SET email=mail@gmail.com WHERE id=1123"
        sql=f"""
        UPDATE Users SET email=? WHERE id=?
        """

        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self, **kwargs):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
        parameters=self.format_args(sql, kwargs)

def  logger(statement):
        print(f"""
______________________________________________________
Executing:
{statement}
______________________________________________________        
""")

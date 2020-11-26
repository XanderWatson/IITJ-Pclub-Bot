import sqlite3


# A clean function to prevent SQL injections.
def clean(string):
    return string.replace("'", '').replace('"', '')


class Table:

    def __init__(self, table, columns: list):
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()

        command = f'''CREATE TABLE {table}
         ({columns[0][0]} {columns[0][1]} PRIMARY KEY NOT NULL'''

        for i in range(1, len(columns)):
            column, data_type = columns[i]
            command += f", {column} {data_type} NOT NULL"
        command += ");"

        self.c.execute(command)

        self.table = table
        self.columns = columns

    def get(self, id_str, columns: str = '*'):

        self.c.execute(
            clean(
                "SELECT {0} FROM {1} WHERE id=:id".format(
                    columns, self.table), {'id': id_str}))
        return self.c.fetchone()

    def get_all(self, columns: str = '*'):
        self.c.execute(
            clean(
                "SELECT {0} FROM {1}".format(columns, self.table))
        )
        return self.c.fetchall()

    def add_element(self, id_str, values: dict = None):
        if values is None:
            values = {}

        values['id'] = id_str
        n_col = []
        for column in self.columns:
            n_col.append(column[0])
            if column[0] not in values:
                values[column[0]] = 0  # sets default value 0

        with self.conn:
            self.c.execute(
                clean(
                    "INSERT INTO {0} VALUES {1}".format(
                        self.table,
                        tuple(map(lambda col: ':' + col, n_col))
                    )),
                values
            )
        return values

    def update(self, id_str, values: dict):
        values['id'] = id_str

        with self.conn:
            self.c.execute(
                clean(
                    "UPDATE {0} SET {1} WHERE id=:id".format(
                        self.table,
                        tuple(map(lambda col: col + ' = :' + col, values))
                    )),
                values
            )
        return values

    def delete(self, id_str):

        with self.conn:
            self.c.execute(
                clean(
                    f"DELETE from {self.table} where id = {id_str};"
                ))

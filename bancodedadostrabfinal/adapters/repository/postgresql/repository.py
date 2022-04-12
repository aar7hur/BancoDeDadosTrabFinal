from psycopg2 import pool


class PostgresqlRepository(object):
    """docstring for PostgresqlRepository."""

    def __init__(self, poolConnect: pool.ThreadedConnectionPool):
        self.__poolConnect = poolConnect
        self.__connection = None

    @property
    def connection(self):

        if not self.__connection:
            self.__connection = self.__poolConnect.getconn()

        return self.__connection

    def cursor(self):
        return self.connection.cursor()

    @staticmethod
    def createWhereSQL(whereList: list, condiction: str = "AND") -> str:

        if len(whereList) <= 0:
            return ""

        condiction = f" {condiction} "

        lines = []

        for where in whereList:
            lines.append(" ".join(where))

        return f"WHERE {condiction.join(lines)}"

    def __del__(self):
        if self.__connection:
            self.__poolConnect.putconn(self.__connection)


if __name__ == "__main__":
    """
    Usage example
    """

    likeList = [["patient_name", "LIKE", "%ana%"]]

    print(PostgresqlRepository.createWhereSQL(likeList))

    booleanList = [["report_id", "IS NOT NULL"]]
    print(PostgresqlRepository.createWhereSQL(booleanList))

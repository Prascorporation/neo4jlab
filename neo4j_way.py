from neo4j import GraphDatabase

class way:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def return_way(self):
        with self.driver.session() as session:
            finding = session.write_transaction(self._find_shortest_path)
            finding.data()

    @staticmethod
    def get_points(self, start, end):
        return self

    @staticmethod
    def _find_shortest_path(tx):
        result = tx.run('use unidb MATCH (p1:home {name: "Home"}), (p2:endpoint {name: "Endpoint"}), path = shortestpath((p1)-[:WAY*]-(p2))RETURN path')

        for i in result.data():
            print(i)

        return result


if __name__ == "__main__":
    way = way("bolt://localhost:7687", "neo4j", "123")
    way.return_way()
   # way.get_points()
    way.close()

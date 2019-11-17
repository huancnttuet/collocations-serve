from app.models import Client


class ClientRepository:
    @staticmethod
    def get_by_id(client_id):
        """ Get Client record by id

        :param client_id: int
        :return: Client
        """
        return Client.query.get(client_id)

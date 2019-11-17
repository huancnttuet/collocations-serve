from app import db
from app.extensions.exceptions.client import ClientNotSaveException, ClientNotFoundException
from app.models import Client
from app.repositories import ClientRepository


class ClientService:
    @staticmethod
    def create_client(data):
        new_client = Client(**data)
        db.session.add(new_client)
        db.session.commit()

        if new_client is None:
            raise ClientNotSaveException
        return new_client

    @staticmethod
    def get_by_id(client_id):
        client = ClientRepository.get_by_id(client_id)

        if client is None:
            raise ClientNotFoundException

        return client

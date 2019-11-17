def register_routes(api, app):
    from app.apis.rating import api as rating_api
    from app.apis.client import api as client_api
    api.add_namespace(rating_api, path="/ratings")
    api.add_namespace(client_api, path="/clients")

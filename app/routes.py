def register_routes(api, app):
    from app.apis.rating import api as rating_api
    from app.apis.client import api as client_api
    from app.apis.uploadfile import api as uploadfile_api
    api.add_namespace(rating_api, path="/ratings")
    api.add_namespace(client_api, path="/clients")
    api.add_namespace(uploadfile_api, path="/uploadfile")

import falcon, json

class NamesResource(object):
    names = [{"id": 1, "name": "Kyle Santiago"}, {"id": 2, "name": "Sandy Sue"}]
    def on_get(self, req, resp):
        resp.body = json.dumps(self.names)

api = falcon.API()
names_endpoint = NamesResource()
api.add_route('/names', names_endpoint)

import falcon
import os

class Index:
    def on_get(self, req, resp):
        resp.content_type = 'text/html'
        resp.body = open('templates/index.html').read()

def _ext_to_media_type(ext):
    return 'image/' + ext

class ImageResource(object):
    def on_get(self, req, resp, filename):
        # do some sanity check on the filename
        resp.status = falcon.HTTP_200
        filename = 'static/images/' + filename
        ext = os.path.splitext(filename)[1][1:]
        resp.content_type = _ext_to_media_type(ext)

        resp.stream = open(filename, 'r')




app = falcon.API()
app.add_route('/', Index())
app.add_route('/static/images/{filename}', ImageResource())


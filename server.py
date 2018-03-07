import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload.html")

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        for form_data_name in self.request.files:
            for file in self.request.files[form_data_name]:
                save = open('uploads/' + file['filename'], 'wb')
                save.write(file['body'])
        self.finish("files is uploaded")

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

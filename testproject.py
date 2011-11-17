#!/usr/bin/env python
import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen

from tornado.options import define, options

from tornadomail.message import EmailMessage
from tornadomail.backends.smtp import EmailBackend

define("port", default=8888, help="run on the given port", type=int)


logging.basicConfig(level=logging.DEBUG) 

class Application(tornado.web.Application):
    @property
    def mail_connection(self):
        return EmailBackend(
            'smtp.gmail.com', 587, '<your google email>', '<your google password>',
            True
        )

class MainHandler(tornado.web.RequestHandler):

    @property
    def mail_connection(self):
        return self.application.mail_connection

    def get(self):
        self.render("index.html")

    def post(self):

        def _finish(num):
            print 'sended %d message(s)' % num
            self.render("index.html")

        message = EmailMessage(
            self.get_argument('subject'),
            self.get_argument('message'),
            '<your google email>',
            [self.get_argument('email')],
            connection=self.mail_connection
        )
        message.send()#callback=_finish)
        self.render("index.html")


def main():
    tornado.options.parse_command_line()
    application = Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

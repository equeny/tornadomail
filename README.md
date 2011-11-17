Tornado mail
============

Asynchronous email sending library for Tornado. Port of django.mail.


Installation
------------

From source: `git clone git://github.com/equeny/tornadomail.git; cd tornadomail; python setup.py install`

Usage
-----

EmailMessage, EmailMultiAlternatives are almost identical to django classes, except send function is async and can receive callback argument.

    from tornadomail.message import EmailMessage, EmailMultiAlternatives
    from tornadomail.backends.smtp import EmailBackend


    class Application(tornado.web.Application):
        @property
        def mail_connection(self):
            return EmailBackend(
                'smtp.gmail.com', 587, '<your google mail>', '<your google password>',
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
                '<your google mail>',
                [self.get_argument('email')],
                connection=self.mail_connection
            )
            message.send()#callback=_finish)
            self.render("index.html")
                                                                                                    
Requirements
------------
The following two python libraries are required

* [tornado>=2.1](http://github.com/facebook/tornado)

Issues
------

Please report any issues via [github issues](https://github.com/equeny/tornadomail/issues)

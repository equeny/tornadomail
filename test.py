# import contextlib

from tornado import ioloop

from tornadomail import send_mail
from tornadomail.backends.smtp import EmailBackend

from tornado import stack_context


def callback(*args, **kwargs):
    callback.count = callback.count + 1
    if callback.count == 5: 
        print 'about to stop ioloop'
        ioloop.IOLoop.instance().stop()
    else: 
        print 'callback count : ', callback.count
    print 'Successfully sent'
    print '*************'

callback.count = 0

def error_handler(e, msg, traceback):
    print 'Error:'
    print msg
    print '**************'
    ioloop.IOLoop.instance().stop()
    return True

l = ['sgp@gmail.com', 'testuser@gmail.com',
     'pqr@gmail.com', 'abc@gmail.com', 'xyz@gmail.com']

with stack_context.ExceptionStackContext(error_handler):
    for to in l:
        print 'to : ', to
        print 'sending mail'
        send_mail(
            'Uber Now', 'Time to book uber', 'anirban.nick@gmail.com',
            [to], callback=callback,
            connection=EmailBackend(
            'smtp.gmail.com', 587, 'username', 'userpassoword,
                True
            )
        )
        print 'mail initiated\n*************\n'

ioloop.IOLoop.instance().start()

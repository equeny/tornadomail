import contextlib

from tornado import ioloop

from tornadomail import send_mail
from tornadomail.backends.smtp import EmailBackend

from tornado import stack_context


def callback(*args, **kwargs):
    ioloop.IOLoop.instance().stop()
    print 'Successfully sended'


def error_handler(e, msg, traceback):
    print 'Error:'
    print msg
    ioloop.IOLoop.instance().stop()
    return True


with stack_context.ExceptionStackContext(error_handler):
    send_mail(
        'subject', 'message', 'robo@djangostars.com',
        ['anton.agafonov@gmail.com'], callback=callback,
        connection=EmailBackend(
            'smtp.gmail.com', 587, 'robo@djangostars.com', 'fakeuser2',
            True
         )
    )

ioloop.IOLoop.instance().start()

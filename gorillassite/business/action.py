import logging

from gorillassite.business.decorator import parameter


__author__ = 'abreu'

logger = logging.getLogger(__name__)


@parameter
class SendMessage:
    """
    Realiza o envio da mensagem por email para
    """

    def __init__(self, slack):

        self.__slack = slack

    def execute(self):

        name = self.parameter['name']
        mail = self.parameter['mail']
        phone = self.parameter['phone']
        message = self.parameter['message']

        full_message = "*%s*\n%s - %s\n\n>>>%s" % (name, mail, phone, message)

        self.__slack.send_message('#contatos', full_message, username='Formulário do Site',
                                  icon_url='https://gorillascode.com/static/imagens/gorillas/baby.jpg')

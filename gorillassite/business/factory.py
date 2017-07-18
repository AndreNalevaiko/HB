import logging

from gorillassite.business import slack


__author__ = 'abreu'

logger = logging.getLogger(__name__)


def send_message_action():

    from gorillassite.business.action import SendMessage

    logger.debug("Instanciando SendMessage(Action) com %s", slack)

    return SendMessage(slack)

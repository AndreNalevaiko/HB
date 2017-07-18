import logging
import os
from flask import Flask
from gorillaspy.logging import config_base_logger
from gorillassite.config import Config

__author__ = 'abreu'

logger = logging.getLogger(__name__)


def wsgi():
    app = Flask(__name__,
                static_folder="web/static",
                template_folder="web/templates")

    app.config.from_object(Config)

    logger.debug('Flask - Configuraçoes OK')

    from gorillassite.web import ui

    app.register_blueprint(ui.app)

    from gorillassite.business import mail

    mail.init_app(app)

    from gorillassite.business import slack

    slack.init_app(app)

    logger.info('App - OK')

    return app


config_base_logger(file_name='logs/gorillassite.log')

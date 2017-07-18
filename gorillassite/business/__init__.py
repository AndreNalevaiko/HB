__author__ = 'abreu'

from flask_mail import Mail

mail = Mail()

from gorillassite.business.integration.slack import Slack

slack = Slack()


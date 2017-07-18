from slacker import Slacker


class Slack:
    """Manages slack integration

    :param app: Flask instance
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.__state = self.init_app(app)
        else:
            self.__state = None

    def init_app(self, app):
        """Initializes your slack settings from the application settings.

        You can use this if you want to set up your Slack instance
        at configuration time.

        :param app: Flask application instance
        """
        self.__state = Slacker(
            app.config.get('SLACK_TOKEN'),
        )

        # register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['slack'] = self.__state

    def send_message(self, channel, text, username=None, as_user=None,
                     parse=None, link_names=None, attachments=None,
                     unfurl_links=None, unfurl_media=None, icon_url=None,
                     icon_emoji=None):

        self.__state.chat.post_message(channel, text, username, as_user, parse,
                                link_names, attachments, unfurl_links,
                                unfurl_media, icon_url, icon_emoji)

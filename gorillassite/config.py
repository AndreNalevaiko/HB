from gorillaspy.config import BaseConfig

__author__ = 'abreu'


class Config(BaseConfig):
    APP_VERSION = '1.0.5'

    DEBUG = False
    SECRET_KEY = "\xba\x19S\xd9\x04\xee\r{\xc15\x16\x87A\xf8\x9d\xcc}\xb3#?\n\xdb\xf0\xf5"

    WTF_CSRF_SECRET_KEY = "4\x89\xcep\x1e\x98\xf6(t9V\xa6\xbd\xcc\x1f\xa3H#\x7f\x8b\x97\xb6\x9b\xcb"

    RECAPTCHA_PUBLIC_KEY = "6LfQRwoTAAAAANKaU30wHRPn74PhRS_IZ5IatA1C"
    RECAPTCHA_PRIVATE_KEY = "6LfQRwoTAAAAAKEhBeNtOjhqNb3nbaRsYcUaX0Jo"

    SLACK_TOKEN = 'xoxp-3581947952-3581947954-39291232437-b5ce0d3c05'

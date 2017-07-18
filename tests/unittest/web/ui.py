import unittest
from unittest.mock import patch

import gorillassite
from tests import mock
import tests.util


__author__ = 'abreu'


class PagesTestCase(unittest.TestCase):

    def setUp(self):

        self.app = gorillassite.wsgi().test_client()

    def test_get_pages(self):

        r = self.app.get('/')
        self.assertIn('Um novo conceito de desenvolvimento', r.data.decode("utf-8"))

        r = self.app.get('/contato')
        self.assertIn('Nós vamos ajudar você', r.data.decode("utf-8"))

        r = self.app.get('/confirmacao')
        self.assertIn('Recebemos sua mensagem', r.data.decode("utf-8"))

    def test_abort_resource(self):

        r = self.app.get('/NAO_EXISTE.html')
        self.assertEqual(r.status_code, 404)

        r = self.app.get('/NAO_EXISTE')
        self.assertEqual(r.status_code, 404)

    def test_get_index(self):

        r = self.app.get('/', follow_redirects=True)
        self.assertIn('Um novo conceito de desenvolvimento', r.data.decode("utf-8"))


class ContactTestCase(unittest.TestCase):

    def setUp(self):

        self.app = gorillassite.wsgi().test_client()

    def test_get_contato(self):

        r = self.app.get('/contato', follow_redirects=True)
        self.assertIn('Nós vamos ajudar você', r.data.decode("utf-8"))

    @patch('gorillassite.business.factory.send_message_action', mock.generic_action)
    def test_post_contato_ok(self):

        # Caminho feliz!

        r = self.app.post('/contato', data=tests.util.dict_contato())

        self.assertIn('Recebemos sua mensagem', r.data.decode("utf-8"))

        # Campos obrigatórios

        r = self.app.post('/contato', data=tests.util.dict_contato(name=False, mail=False, message=False))

        self.assertIn('Nome é obrigatório', r.data.decode("utf-8"))
        self.assertIn('Email é obrigatório', r.data.decode("utf-8"))
        self.assertIn('Mensagem é obrigatória', r.data.decode("utf-8"))

        # Email formato invalido

        r = self.app.post('/contato', data=tests.util.dict_contato(invalid_mail=True))

        self.assertIn('Email inválido', r.data.decode("utf-8"))

    @patch('gorillassite.business.factory.send_message_action', mock.generic_action_boom)
    def test_post_contato_exception(self):

        # Exceçao ao executar action sendmail

        r = self.app.post('/contato', data=tests.util.dict_contato())

        self.assertIn('Opssss ocorreu um imprevisto!', r.data.decode("utf-8"))

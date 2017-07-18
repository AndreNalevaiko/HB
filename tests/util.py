__author__ = 'abreu'


def dict_contato(name=True, mail=True, phone=True, company=True, message=True, invalid_mail=False):

    post_form = {
        'name': 'Rafael Abreu',
        'mail': 'rafael.abreu@gmail.com',
        'phone': '4130276049',
        'company': 'Gorilla\'s Code',
        'message': 'Mensagem Teste!'
    }

    if not name:
        del post_form['name']

    if not mail:
        del post_form['mail']

    if not phone:
        del post_form['phone']

    if not company:
        del post_form['company']

    if not message:
        del post_form['message']

    if invalid_mail:
        post_form['mail'] = 'rafael.abreugmail.com'

    return post_form

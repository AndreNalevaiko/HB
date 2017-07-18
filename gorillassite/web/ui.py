import logging
import os

from flask import Blueprint, redirect
from flask.globals import request
from flask.helpers import send_from_directory
from flask.templating import render_template
from gorillassite.business import factory
from gorillassite.web import form
from jinja2.exceptions import TemplateNotFound


__author__ = 'abreu'

logger = logging.getLogger(__name__)

app = Blueprint('view', __name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/png')


@app.route('/robots.txt')
def robots():

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt', mimetype='text/plain')


@app.route('/assinatura')
def get_mail_signature():

    return render_template("assinatura.html",
                           name=request.args.get('name'),
                           titles=request.args.get('titles'),
                           phone=request.args.get('phone'))


@app.route('/contatos/<contato>')
def contatos(contato):

    logger.debug("Resolvendo página %s", contato)

    return redirect("/")


@app.route('/<page>')
def get_pages(page):

    logger.debug("Resolvendo página %s", page)

    return render_template(page+".html")


@app.route('/')
@app.route('/index.html')
def get_index():

    logger.debug("Redirecionando para index.html")

    return render_template("/index.html")


@app.route('/infos')
def get_infos():

    logger.debug("Obtém as informações a serem utilizadas")

    return render_template("/infos.json")


@app.route('/contato')
def get_contact():

    logger.debug("Resolvendo página contato")

    return render_template("contato.html", form=form.Contact())


@app.route('/contato', methods=['POST'])
def post_contact():
    """
    Recebe os posts dos contatos enviados pelo formulário do site
    """

    contact_form = form.Contact(request.form)

    logger.debug("Recebendo post contato %s", contact_form)

    if contact_form.validate():

        logger.debug("Formulário validado")

        action = factory.send_message_action()

        action.add_parameter(
            name=contact_form.name.data,
            mail=contact_form.mail.data,
            phone=contact_form.phone.data,
            message=contact_form.message.data)

        action.execute()

        return render_template("confirmacao.html", mail=contact_form.mail.data)

    return render_template("contato.html", form=contact_form)


@app.errorhandler(TemplateNotFound)
def handle_template_not_found(e):

    logger.error("Capturado TemplateNotFound", e)

    return handle_404(e)


@app.errorhandler(Exception)
def handle_exception(e):

    logger.error("Capturado Exception", e)

    return render_template("500.html"), 500


@app.errorhandler(404)
def handle_404(e):

    logger.error("Capturado 404 Not found", e)

    return render_template("404.html"), 404

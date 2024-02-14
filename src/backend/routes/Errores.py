from flask import Blueprint, render_template

Errors = Blueprint("Errors", __name__)


@Errors.app_errorhandler(404)
def page_not_found(error):
    return render_template("err/404.html"), 404

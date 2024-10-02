"""Main Routes for the Application"""


from flask import Blueprint, render_template, send_from_directory


main_blueprint = Blueprint('main', __name__, template_folder='templates/main')


@main_blueprint.route('/')
def index():
    """Render the main dashboard template"""
    return render_template('main/dashboard.html')


@main_blueprint.route('/favicon.ico')
def favicon():
    """Serve the favicon"""
    return send_from_directory('static', 'favicon.ico')


@main_blueprint.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@main_blueprint.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500
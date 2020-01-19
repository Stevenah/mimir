import flask

mod = flask.Blueprint('pages', __name__)

@mod.route('/', defaults={'path': ''})
@mod.route('/<path:path>')
def catch_all(path):
    """ Catch all paths and return index.html.

        # Returns
            index.html.
    """
    return flask.render_template('index.html')
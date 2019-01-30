from webapp.app import app
from webapp.app.models import Test

@app.shell_context_processor
def make_shell_context():
    return {'Test': Test}

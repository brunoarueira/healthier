from flask import Blueprint, Response

mod = Blueprint('status', __name__)


@mod.route('/api/health_check')
def health_check():
    return Response(mimetype='application/json', status=200)

from functools import wraps
from flask_login import  current_user
from . import login_manager

def admin_required():
    def admin_required(f):
        @wraps(f)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if not current_user.is_admin():
                return 'Forbidden', 403
            return f(*args, **kwargs)
        return decorated_view
    return admin_required
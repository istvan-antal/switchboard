import datetime
from flask import current_app, abort, request
from functools import update_wrapper

def hmac_auth(rights=None):
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            try:
                timestamp = request.values.get('TIMESTAMP')
                assert timestamp is not None
            except:
                current_app.logger.info("hmac_auth failure - no timestamp supplied")
                abort(403)

            ts = datetime.datetime.fromtimestamp(float(timestamp))

            #  is the timestamp valid?
            if ts < datetime.datetime.now()-datetime.timedelta(seconds=5) \
                    or ts > datetime.datetime.now():
                current_app.logger.info("hmac_auth failure - invalid timestamp")
                abort(403)

            if current_app.hmac_manager.is_authorized(request, rights):
                return f(*args, **kwargs)
            else:
                # TODO: make this custom,
                # maybe a current_app.hmac_manager.error() call?
                current_app.logger.info("hmac_auth failure - invalid credentials")
                abort(403)
        return update_wrapper(wrapped_function, f)
    return decorator
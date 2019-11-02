from flask import request, make_response
import jwt
from utils import get_env, create_response

# setting up
auth_key = get_env("AUTHKEY", "DEFAULT")
with open("api/whitelist.txt", 'r') as wl:  # TODO: MAY NOT WORK BECAUSE RELATIVE PATH
    whitelist = [i.rstrip() for i in wl.readlines()]

print(whitelist, " are whitelisted")


def mw(handler):
    def auth(*args, **kwargs):
        host = list(request.host.split(':'))[0]
        jwt_present = "jwt_token" in request.cookies.keys()
        # 0) check if jwt_token is_valid
        if jwt_present:
            jwt_token = request.cookies.get("jwt_token")
            try:
                decoded_token = jwt.decode(jwt_token, auth_key, algorithms='HS256')
            except jwt.exceptions:
                decoded_token = None
            if decoded_token is None:  # 0.5) if not valid, just delete it => rewrite the cookie
                jwt_present = False
            elif decoded_token.get("ip") in whitelist:
                # print("GAINED ACCESS THROUGH COOKIE")
                return make_response(handler(*args, **kwargs))

        if not jwt_present:
            if host in whitelist:
                # print("GAINED ACCESS THROUGH WHITELIST")
                resp = make_response(handler(*args, **kwargs))
                new_token = str(jwt.encode({"ip": host}, auth_key, algorithm='HS256')) \
                    .lstrip("b\'").rstrip('\'')
                resp.set_cookie("jwt_token", new_token)
                return resp
            else:
                # print(host, " IS NOT WHITELISTED")
                return make_response(create_response(False, "NOT WHITELISTED"), 401)

    return auth

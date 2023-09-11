from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200
       

def search_users(key_dict): 

    results = []

    def partial_match(value, keyword):
        return keyword.lower() in value.lower()

    for user in USERS:
        include_user = True

        if 'id' in key_dict and key_dict['id'] == user['id'].values():
            results.append(user)
            continue

        if 'name' in key_dict:
            name_keywords = key_dict['name'].split()
            if not any(partial_match(user['name'], keyword) for keyword in name_keywords):
                include_user = False

        if 'age' in key_dict:
            age = int(key_dict['age'])
            if not (age - 1 <= user['age'] <= age + 1):
                include_user = False

        if 'occupation' in key_dict:
            if not partial_match(user['occupation'], key_dict['occupation']):
                include_user = False

        if include_user:
            results.append(user)

    return results

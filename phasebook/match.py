import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match Found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200
    
def is_match(left_list, right_list):
   
    left_list.sort()
    right_list.sort()

    left = 0 

    right = len(left_list) - 1

    for x in right_list:

        while left <= right:

            mid  = (left + right) // 2

            if left_list[mid] == x:
                return True
            elif left_list[mid] < x:
                left = mid + 1
            else:
                right = mid -1

        return False
 
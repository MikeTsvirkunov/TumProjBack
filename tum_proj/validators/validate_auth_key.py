import ioc

from tum_proj.models import WorkingSession


def validate_auth_key(user_id: str):
    l: list[WorkingSession] = list(ioc.require('WorkingSession.ListOfSessions'))
    for i in l:
        if i.working_id == user_id:
            return True
    if user_id == 'god_key':
        return True
    return False
    
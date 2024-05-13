import ioc
from tum_proj.builders.build_pull_request_model import build_pull_rquest_model
from tum_proj.builders.build_user_model import test_build_user_model
from tum_proj.getters.get_last_checked_pr import get_last_checked_pr
from tum_proj.getters.get_list_of_pr import test_get_list_of_pr
from tum_proj.getters.get_registration_code import uuid_registration_code_getter
from tum_proj.getters.get_user import get_user_by_validation_code
from tum_proj.savers.save_pr import test_save_pr
from tum_proj.validators.registration_code_validation import registration_code_validator
from tum_proj.validators.registration_validation import test_registration_validator
from tum_proj.validators.validate_past_pr_is_checked import test_validate_past_pr_is_checked


def values_initiation():
    ioc.provide('GitHub.Request.Parser', 'html.parser')
    ioc.provide('dict_of_registrated_users', dict())
    ioc.provide('list_of_pr', list())
    ioc.provide('dict_of_last_past_checked_pr', dict())
    ioc.provide('GitHub.Request.Header', {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'})


def functions_initialization():
    ioc.provide('build_pull_rquest_model', build_pull_rquest_model)
    ioc.provide('get_user_by_validation_code', get_user_by_validation_code)
    ioc.provide('save_pr', test_save_pr)
    ioc.provide('validate_past_pr_is_checked', test_validate_past_pr_is_checked)
    ioc.provide('get_list_of_pr', test_get_list_of_pr)
    ioc.provide('get_last_checked_pr', get_last_checked_pr)
    ioc.provide('registration_validator', test_registration_validator)
    ioc.provide('build_user_model', test_build_user_model)
    ioc.provide('registration_code_getter', uuid_registration_code_getter)
    ioc.provide('registration_code_validator', registration_code_validator)
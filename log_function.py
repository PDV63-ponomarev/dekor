import types
from functools import wraps

def humanify(name:str) -> str:
    import re
    return ' '.join(re.split('_+', name))


def step(fn):
    @wraps(fn)
    def fn_with_logging(*args, **kwargs) :
       is_method = (
            args
            and isinstance(args[0], object)
            and isinstance(getattr(args[0], fn.__name__), types.MethodType)
        )

       args_to_log = args[1:] if is_method else args
       args_and_kwargs_to_log_as_strings = [
            *map(str, args_to_log),
            *[f'{key}={value}' for key, value in kwargs.items()]
        ]
       args_and_kwargs_strings = (
            (': ' + ', '.join(map(str, args_and_kwargs_to_log_as_strings)))
            if args_and_kwargs_to_log_as_strings
            else ''
        )

       print(
            (f'[{args[0].__class__.__name__}] ' if is_method else '')
            + humanify(fn.__name__)
            + args_and_kwargs_strings
        )

       return fn(*args, **kwargs)

    # fn_with_logging.__name__ = fn.__name__

    return fn_with_logging

'''
@step
def given_sign_uo_form_opened():
    log_step(given_sign_uo_form_opened.__name__)
 
 
тоже самое

def given_sign_uo_form_opened():
    log_step(given_sign_uo_form_opened.__name__)
given_sign_uo_form_opened = step(given_sign_uo_form_opened)      
'''

@step('Open registration form')
def given__sign_uo_form_opened():
    # print(given__sign_uo_form_opened.__name__)
    ...


class SignUpForm:
    @step
    def fill_name(self, first_name, last_name):
        pass

    @step
    def fill_email(self, value):
        pass

    @step
    def fill_password(self, value):
        pass

    @step
    def submit(self):
        pass


class DashBoard:
    @step
    def go_to_profile(self):
        pass

sign_up_form = SignUpForm()
dashboard = DashBoard()


given__sign_uo_form_opened()
sign_up_form.fill_name('dima', last_name='ponomarev')
sign_up_form.fill_email(value='test@mail.com')
sign_up_form.fill_password('qwerty')
sign_up_form.submit()
dashboard.go_to_profile()



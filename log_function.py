

def sentencify(name:str) -> str:
    import re
    ' '.join(re.split('_+', name))


def step(fn):
    def fn_with_logging(*args, **kwargs) :
        fn_name = sentencify(fn.__name__)
        print(
            fn_name
            + ', '.join(map(str, args)) if args else ''
        )
        return fn(*args, **kwargs)

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

@step
def given__sign_uo_form_opened():
    # log_step(given__sign_uo_form_opened.__name__)
    pass


class SignUpForm:
    @step
    def fill_email(self, value):
        # log_step(self.fill_email.__name__)
        pass

    @step
    def fill_password(self, value):
        # log_step(self.fill_password.__name__)
        pass

    @step
    def submit(self):
        # log_step(self.submit.__name__)
        pass


class DashBoard:
    @step
    def go_to_profile(self):
        # log_step(self.go_to_profile.__name__)
        pass

sign_up_form = SignUpForm()
dashboard = DashBoard()


given__sign_uo_form_opened()
sign_up_form.fill_email('test@mail.com')
sign_up_form.fill_password('qwerty')
sign_up_form.submit()
dashboard.go_to_profile()



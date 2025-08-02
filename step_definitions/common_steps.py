from pytest_bdd import given, when, then, parsers

@given(parsers.parse('user is on Login Page'))
def user_on_login_page():
    pass

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(username, password):
    pass

@when('user clicks Login Button')
def user_clicks_login():
    pass

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_has_text(text):
    pass

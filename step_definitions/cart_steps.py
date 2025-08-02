from pytest_bdd import when, then

@when('user adds first product to cart')
def user_adds_first_product():
    pass

@when('user clicks cart icon')
def user_clicks_cart_icon():
    pass

@then('verify cart page has text "Your Cart"')
def verify_cart_page():
    pass

@then('verify cart contains items')
def verify_cart_contains_items():
    pass

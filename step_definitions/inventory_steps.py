from pytest_bdd import when, then

@when('user clicks Sort Icon')
def user_clicks_sort_icon():
    pass

@when('user clicks Sort the Products by Name (A–Z)')
def user_clicks_sort_by_name():
    pass

@then('all the products must be sorted from A to Z')
def verify_products_sorted():
    pass

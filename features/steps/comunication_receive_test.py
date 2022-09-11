from behave import given, when, then


@then("the app should receive the address \"{address}\" and value \"{value}\"")
def then_the_app_receive_the_address_and_value(context, address, value):
    response = Response.from_bytes(context.response)

    assert response.get_function() == address
    assert response.get_value() == value

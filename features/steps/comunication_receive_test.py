from behave import given, when, then
from src.models import Response


@then("the app should receive the address \"{address}\" and value \"{value}\"")
def then_the_app_receive_the_address_and_value(context, address, value):
    print(context.response)
    response = Response()
    Response.from_bytes(response, context.response)

    assert response.get_function() == address
    assert response.get_value() == value

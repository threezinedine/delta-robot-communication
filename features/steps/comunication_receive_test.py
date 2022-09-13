from behave import given, when, then
from src.models import Response

@then("the app should receive the address \"{address}\" and value \"{value}\"")
def then_the_app_receive_the_address_and_value(context, address, value):
    print(context.response)
    response_obj = Response()
    Response.from_bytes(response_obj, context.response)

    print(type(value))
    assert response_obj.get_function() == int(address)
    assert response_obj.get_value() == int(value)

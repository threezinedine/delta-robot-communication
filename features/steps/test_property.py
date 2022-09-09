from behave import given, when, then
from src.models import Property


@given("The property has {num_bytes} bytes")
def given_property_num_bytes(context, num_bytes:int):
    context.test_property = Property(num_bytes=int(num_bytes))

@when("The property converts {decimal_number}")
def when_property_converts_number(context, decimal_number:int):
    context.result = context.test_property.converts_decimal_number_to_hex_string(int(decimal_number))

@then("We should see the result: {expected}")
def then_assert_the_expected_result(context, expected):
    assert context.result == expected


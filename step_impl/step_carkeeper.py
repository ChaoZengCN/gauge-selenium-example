from getgauge.python import step, before_scenario, Messages
from step_impl.pages.activity_new import Activity_New

class TestCase:
    Activity_New = Activity_New()

@step("login")
def assert_login():
    status = TestCase.Activity_New.login()
    assert status
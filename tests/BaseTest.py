import pytest
from utilities.ReadConfigurations import ReadConfig   # Import configuration reader
from utilities.customLogger import LogGen             # Import custom logger


@pytest.mark.usefixtures("setup_and_teardown")  # Apply setup and teardown fixture
class BaseTest:
    # Read test data from config file
    url = ReadConfig.get_application_url()          # Application URL
    username = ReadConfig.get_username()            # Valid username
    password = ReadConfig.get_password()            # Valid password
    invalid_username = ReadConfig.get_invalid_username()  # Invalid username
    problem_user = ReadConfig.get_problem_user()          # Problem user
    performance_glitch_user = ReadConfig.get_performance_glitch_user()  # Performance glitch user
    locked_out_user = ReadConfig.get_locked_out_user()    # Locked out user
    visual_user = ReadConfig.get_visual_user()            # Visual user
    error_user = ReadConfig.get_error_user()              # Error user

    # Initialize logger
    logger = LogGen.loggen()
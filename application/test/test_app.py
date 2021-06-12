import click
from flask.cli import with_appcontext
from application.models import User


@click.command(name='test')
@with_appcontext
def test_func():
    test_user()
    test_home_page()


def test_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and username
    """
    user = User(
        username='User000',
        email='User000@gmail.com',
        password='Password',
        role='user'
        )
    assert user.username == 'User000'
    assert user.email == "User000@gmail.com"


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    from application import init_app
    flask_app = init_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
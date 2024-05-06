from src.auth.auth import auth_backend


def test_get_backends():
    assert auth_backend.name == "jwt"
    assert auth_backend.transport.scheme.scheme_name == "APIKeyCookie"
    assert auth_backend.get_strategy().algorithm == "HS256"

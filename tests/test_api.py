from src.api import app


def test_server():
    paths = [path for path in app.openapi()["paths"].keys()]

    assert "/auth/jwt/login" in paths
    assert "/auth/jwt/logout" in paths
    assert "/auth/register" in paths

    assert "/users/" in paths
    assert "/users/update" in paths

    assert "/posts/" in paths
    assert "/posts/update" in paths

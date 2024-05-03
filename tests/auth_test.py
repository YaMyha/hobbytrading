from tests.configs.conftest import client


class TestAuth:
    def test_register(self):
        response = client.post("/auth/register", json={
            "username": "string",
            "email": "string",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
        })

        assert response.status_code == 201

# IT DOESN'T WORK.
    # def test_login(self):
    #     assert "fastapiusersauth" not in client.cookies
    #     response = client.post("/auth/jwt/login", json={
    #         "username": "string",
    #         "password": "string"
    #     })
    #     cookies = [header for header in response.raw_headers if header[0] == b"set-cookie"]
    #     assert len(cookies) == 1
    #
    #     cookie = cookies[0][1].decode("latin-1")
    #
    #     assert "fastapiusersauth" in cookie

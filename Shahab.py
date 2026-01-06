import requests

BASE_URL = "http://10.3.10.104:3000"


def main():
    try:
        # 1. Hämta token
        token_response = requests.post(f"{BASE_URL}/api/token")
        token_response.raise_for_status()
        token = token_response.json().get("token")
        if not token:
            print("Token saknas i svaret.")
            return

        # 2. Verifiera token
        headers = {"Authorization": f"Bearer {token}"}
        verify_response = requests.post(f"{BASE_URL}/api/verify", headers=headers)
        verify_response.raise_for_status()
        secret = verify_response.json().get("secret")
        if not secret:
            print("Secret saknas i svaret.")
            return

        flag_response = requests.post(
            f"{BASE_URL}/api/flag", headers=headers, json={"secret": secret}
        )
        flag_response.raise_for_status()
        flag = flag_response.json().get("flag")
        if not flag:
            print("Flagga saknas i svaret.")
            return

        print("FLAGGA:", flag)

    except requests.RequestException as e:

        print("Ett fel uppstod vid anropet till API:", e)
    except Exception as e:

        print("Ett oväntat fel uppstod:", e)


if __name__ == "__main__":
    main()

import requests

def main():
    api_url = "https://hire-game.netsach.dev/api/v1.1/"

    headers = {
        "Content-Type": "application/json"    }

    # 1- Register
    register_data = {
        "email": "ramdanimeriem001@gmail.com",
        "password1": "api123",
        "password2": "api123"
    }

    register_url = api_url + "auth/register/"

    response = requests.post(register_url, json=register_data, headers=headers)

    if response.status_code == 201:
        print("Inscription réussie.")

        # 2-Login
        login_data = {
            "email": "ramdanimeriem001@gmail.com",
            "password": "api123"
        }

        login_url = api_url + "auth/login/"

        response = requests.post(login_url, json=login_data, headers=headers)

        if response.status_code == 200:
            login_response = response.json()
            token = login_response.get("token", "")
            print("Connexion réussie. Token :", token)
            headers = {
                        "Content-Type": "application/json",
                        "Authorization": f"Token {token}"
            }

            # 3-Create application
            application_data = {
                "email": "ramdanimeriem001@gmail.com",
                "first_name": "meriem",
                "last_name": "ramdani"
            }
            
            application_url = api_url + "job-application-request/"

            response = requests.post(application_url, json=application_data, headers=headers)

            if response.status_code == 201:
                application_response = response.json()
                application_url = application_response.get("url", "")
                print("Application crée avec succès :", application_url)

                # application status
                while application_response.get("status") != "COMPLETED":
                    response = requests.get(application_url, headers=headers)
                    application_response = response.json()
                print("Statut de l'application :", application_response.get("status"))
                confirmation_url = application_response.get("confirmation_url", "")
                print("Confirmation URL :", confirmation_url)

                # 5-Confirm application
                confirm_data = {
                    "confirmed": True
                }

                confirm_response = requests.patch(confirmation_url, json=confirm_data, headers=headers)

                if confirm_response.status_code == 200:
                    print("Confirmation de l'application réussie.")
                else:
                    print("Échec de la confirmation de l'application :", confirm_response.text)
            else:
                print("Échec de la création de la demande d'application :", response.text)
        else:
            print("Échec de la connexion :", response.text)
    else:
        print("Échec de l'inscription :", response.text)

if __name__ == "__main__":
    main()

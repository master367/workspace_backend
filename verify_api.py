import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def verify():
    print("--- Verifying API ---")
    
    # 1. Login (using form-data as Swagger does)
    login_data = {
        "username": "admin@example.com",
        "password": "adminpassword123"
    }
    
    try:
        print(f"Attempting login (Form Data) at {BASE_URL}/auth/login...")
        response = requests.post(f"{BASE_URL}/auth/login", data=login_data)
        if response.status_code == 200:
            token = response.json().get("access_token")
            print("Login successful! Token received.")
            
            # 2. Get me
            headers = {"Authorization": f"Bearer {token}"}
            print(f"Attempting /auth/me with token...")
            me_response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
            if me_response.status_code == 200:
                print("Profile retrieval successful!")
                print(json.dumps(me_response.json(), indent=2))
            else:
                print(f"Profile retrieval failed: {me_response.status_code} - {me_response.text}")
        else:
            print(f"Login failed: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    verify()

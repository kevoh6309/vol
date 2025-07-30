import requests
from bs4 import BeautifulSoup

base_url = "http://127.0.0.1:5000"

def check_form_action():
    """Check the form action in the resume form"""
    session = requests.Session()
    
    print("🔍 Checking resume form action...")
    
    # Login first
    response = session.get(f"{base_url}/login")
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})
    
    if csrf_token:
        login_data = {
            'csrf_token': csrf_token.get('value'),
            'email': 'resumetestuser@example.com',
            'password': 'testpass123'
        }
        
        response = session.post(f"{base_url}/login", data=login_data)
        if response.status_code == 200:
            print("✅ Login successful")
            
            # Get create resume page
            response = session.get(f"{base_url}/create-resume")
            if response.status_code == 200:
                print("✅ Create resume page accessible")
                
                soup = BeautifulSoup(response.text, 'html.parser')
                form = soup.find('form')
                
                if form:
                    action = form.get('action')
                    method = form.get('method')
                    print(f"   Form action: {action}")
                    print(f"   Form method: {method}")
                    
                    if action == '/create-resume':
                        print("   ✅ Form action is correct")
                    else:
                        print(f"   ❌ Form action should be /create-resume, but is {action}")
                else:
                    print("   ❌ No form found")
            else:
                print("❌ Cannot access create resume page")
        else:
            print("❌ Login failed")
    else:
        print("❌ No CSRF token found")

if __name__ == "__main__":
    check_form_action() 
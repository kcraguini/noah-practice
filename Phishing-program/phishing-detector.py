""""
Find/download phishing datasets
Clean and organize the data
Remove duplicates, handle missing values
Create a labeled dataset (phishing vs. legitimate)
Exploratory data analysis (EDA) — understand patterns
Prepare the data in a standardized format (CSV)
link to the claude convo: https://claude.ai/share/c16d69ce-2a7c-446c-a390-e43192c35e20
"""
print("Henlo")
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_api_python_client import discovery

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    """
    Authenticate user with Gmail and return service object.
    First time: opens browser for login
    After that: uses saved credentials
    """
    creds = None
    
    # Load saved credentials if they exist
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If no valid credentials, get new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # User logs in here (browser opens automatically)
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next time
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return discovery.build('gmail', 'v1', credentials=creds)

def fetch_emails(service, max_results=10):
    """
    Fetch emails from user's inbox.
    Returns list of emails with subject and body
    """
    try:
        results = service.users().messages().list(
            userId='me', 
            q='in:inbox',  # Get from inbox
            maxResults=max_results
        ).execute()
        
        messages = results.get('messages', [])
        emails = []
        
        for message in messages:
            msg = service.users().messages().get(
                userId='me', 
                id=message['id'],
                format='full'
            ).execute()
            
            headers = msg['payload']['headers']
            subject = next(
                (h['value'] for h in headers if h['name'] == 'Subject'),
                'No Subject'
            )
            
            # Get email body (simplified)
            if 'parts' in msg['payload']:
                body = msg['payload']['parts'][0]['body'].get('data', '')
            else:
                body = msg['payload']['body'].get('data', '')
            
            emails.append({
                'id': message['id'],
                'subject': subject,
                'body': body
            })
        
        return emails
    
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []

if __name__ == '__main__':
    # This runs when you execute the script
    print("Authenticating with Gmail...")
    service = authenticate_gmail()
    
    print("Fetching emails...")
    emails = fetch_emails(service, max_results=5)
    
    print(f"\nFetched {len(emails)} emails:")
    for i, email in enumerate(emails, 1):
        print(f"\n{i}. Subject: {email['subject']}")
        print(f"   Body preview: {email['body'][:100]}...")
import sendgrid
from sendgrid.helpers.mail import Mail, Content

def send_email(sendgrid_api_key, subject, body, from_email = 'psusann.01@gmail.com', recipients = ['jamie.o-brien@ucdconnect.ie']):

    """
    A function to send emails using the sendgrid service
    
    Parameters
    ----------
    subject: string
        The subject of the email.
        
    body: string
        The body of text for the email.

    from_email: string
        The email to be used to send the email (this should be set up on the sendgrid website when setting up the sendgrid api key).

    recipients: list
        A list of email addresses to send the email to.
        
    sendgrid_api_key: string
        The verified sendgrid api key associated with the sender email.
    
    Returns
    -------
    None
    """
    
    # Create the content to be sent in the email
    content = Content("text/plain", str(body))
    
    # Compile the email info as a Mail object
    mail = Mail(from_email, recipients, str(subject), content)
    
    try:
        sg = sendgrid.SendGridAPIClient(sendgrid_api_key)
        response = sg.client.mail.send.post(request_body=mail.get())

    except Exception as e:
        print("ERROR")
        print(e.message)
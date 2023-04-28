from django.core.mail import send_mail
from account.models import User


def send_spam(new_product):
    users_email = [x.email for x in User.objects.all()]
    message = f"""
    U nas poyavilsya novyi produkt
    
    {new_product.title}
    
    {new_product.description}
    """
    send_mail("Novinka", message, "a@gmail.com", users_email)

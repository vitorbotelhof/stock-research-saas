import stripe
from fastapi import HTTPException

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

async def create_lifetime_subscription(email: str):
    try:
        customer = stripe.Customer.create(email=email)
        payment_intent = stripe.PaymentIntent.create(
            amount=9900,  # $99.00
            currency="usd",
            customer=customer.id,
            description="Lifetime Access Purchase"
        )
        return payment_intent.client_secret
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

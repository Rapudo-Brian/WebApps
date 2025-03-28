from rest_framework.response import Response
from rest_framework.decorators import api_view
from decimal import Decimal

# Hardcoded exchange rates
EXCHANGE_RATES = {
    ('GBP', 'EUR'): Decimal('1.16'),
    ('GBP', 'USD'): Decimal('1.38'),
    ('EUR', 'GBP'): Decimal('0.86'),
    ('EUR', 'USD'): Decimal('1.18'),
    ('USD', 'GBP'): Decimal('0.72'),
    ('USD', 'EUR'): Decimal('0.85'),
}

@api_view(['GET'])
def currency_conversion(request, currency1, currency2, amount):
    try:
        amount = Decimal(amount)
        if (currency1, currency2) in EXCHANGE_RATES:
            rate = EXCHANGE_RATES[(currency1, currency2)]
            converted_amount = round(amount * rate, 2)
            return Response({'converted_amount': converted_amount, 'rate': rate})
        elif currency1 == currency2:
            return Response({'converted_amount': amount, 'rate': 1})
        else:
            return Response({'error': 'Unsupported currency pair'}, status=400)
    except ValueError:
        return Response({'error': 'Invalid amount'}, status=400)

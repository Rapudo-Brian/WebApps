from rest_framework.response import Response
from rest_framework.decorators import api_view

# Hardcoded exchange rates
EXCHANGE_RATES = {
    ('GBP', 'EUR'): 1.16,
    ('GBP', 'USD'): 1.38,
    ('EUR', 'GBP'): 0.86,
    ('EUR', 'USD'): 1.18,
    ('USD', 'GBP'): 0.72,
    ('USD', 'EUR'): 0.85,
}

@api_view(['GET'])
def currency_conversion(request, currency1, currency2, amount):
    try:
        amount = float(amount)
        if (currency1, currency2) in EXCHANGE_RATES:
            rate = EXCHANGE_RATES[(currency1, currency2)]
            converted_amount = round(amount * rate, 2)
            return Response({'converted_amount': converted_amount, 'rate': rate})
        else:
            return Response({'error': 'Unsupported currency pair'}, status=400)
    except ValueError:
        return Response({'error': 'Invalid amount'}, status=400)

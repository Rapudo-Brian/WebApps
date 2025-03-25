from django.http import JsonResponse

# Hardcoded exchange rates (example rates)
EXCHANGE_RATES = {
    "GBP": {"USD": 1.3, "EUR": 1.15},
    "USD": {"GBP": 0.77, "EUR": 0.89},
    "EUR": {"GBP": 0.87, "USD": 1.12},
}


def convert_currency(request, currency1, currency2, amount):
    try:
        amount = float(amount)
        if currency1 not in EXCHANGE_RATES or currency2 not in EXCHANGE_RATES[currency1]:
            return JsonResponse({"error": "Unsupported currency"}, status=400)

        converted_amount = round(amount * EXCHANGE_RATES[currency1][currency2], 2)
        return JsonResponse({
            "from_currency": currency1,
            "to_currency": currency2,
            "original_amount": amount,
            "converted_amount": converted_amount
        })

    except ValueError:
        return JsonResponse({"error": "Invalid amount"}, status=400)

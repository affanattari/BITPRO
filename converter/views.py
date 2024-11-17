from django.shortcuts import render

# Create your views here.
# converter/views.py

from django.shortcuts import render
from .utils import (
    decimal_to_binary, decimal_to_octal, decimal_to_hexadecimal,
    binary_to_decimal, octal_to_decimal, hexadecimal_to_decimal
)


def index(request):
    if request.method == 'POST':
        input_value = request.POST.get('input_value')
        input_base = request.POST.get('input_base')
        output_base = request.POST.get('output_base')

        # Convert input to decimal
        decimal_value = 0
        try:
            if input_base == 'decimal':
                decimal_value = int(input_value)
            elif input_base == 'binary':
                decimal_value = binary_to_decimal(input_value)
            elif input_base == 'octal':
                decimal_value = octal_to_decimal(input_value)
            elif input_base == 'hexadecimal':
                decimal_value = hexadecimal_to_decimal(input_value)
        except ValueError:
            return render(request, 'converter/index.html', {
                'error': "Invalid input for the selected base."
            })

        # Convert from decimal to target base
        if output_base == 'binary':
            result = decimal_to_binary(decimal_value)
        elif output_base == 'octal':
            result = decimal_to_octal(decimal_value)
        elif output_base == 'hexadecimal':
            result = decimal_to_hexadecimal(decimal_value)
        else:
            result = str(decimal_value)

        return render(request, 'converter/index.html', {
            'result': result,
            'input_value': input_value,
            'input_base': input_base,
            'output_base': output_base
        })

    return render(request, 'converter/index.html')

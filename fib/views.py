import time
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render


class FibView(View):
    def get(self, request, *args, **kwargs):
        start = time.clock()
        num = request.GET.get('number', '')
        if num.isdigit():
            number = int(0 if num is None else num)
            result = self.fibonacci(number)
            end = time.clock()
            elapsed = end - start
            fib_result = {'number': number, 'result': result, 'elapsed': elapsed}
            return render(request, 'fibonacci.html', {'fib_result': fib_result})
        else:
            return render(request, 'fibonacci.html')

    def fibonacci(self, number):
        a = 1
        b = 1
        c = a + b
        count = 2
        while number > count:
            c = a + b
            a = b
            b = c
            count = count + 1
        return c

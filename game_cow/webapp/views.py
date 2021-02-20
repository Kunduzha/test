from django.shortcuts import render


def cow_game(request):
    secret_nums = [5, 1, 2, 9]
    if request.method=='GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        context = {}
        numbers_list = request.POST.get("numbers")
        try:
            numbers = list(map(int, numbers_list.split(' ')))
            if len(numbers) != len(secret_nums):
                context["result"] = f'Введите 4 числа через пробелы'
            context["result"] = guess_numbers(secret_nums, numbers)

        except ValueError:
            context["result"] += f'Нужно ввести только числа'
        except KeyError:
            context["result"] += f'Нужно ввести только числа'

        return render(request, 'index.html', context)


def guess_numbers(secret_nums, numbers):
    cow = 0
    bull = 0
    for i in range(len(numbers)):
        if numbers[i] in numbers[i + 1:]:
            return 'Цифры не должны повторяться'
        if numbers[i] > 10 or numbers[i] < 0:
            return ' Введите числа больше 0 и меньше 10 '
        if secret_nums[i] == numbers[i]:
            bull += 1
        elif numbers[i] in secret_nums:
            cow += 1
    return f'коров {cow} шт,бык: {bull} шт'



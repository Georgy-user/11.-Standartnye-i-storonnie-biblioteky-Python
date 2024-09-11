import numpy
import matplotlib.pyplot
import requests
from time import sleep

# Работа с библиотекой numPy.
print('Работа с библиотекой numPy.')


def matrix_comparer(m_1, m_2):  # Сравнение матриц (поэлементное).
    compar = True
    for i in range(m_1.shape[0]):
        for j in range(m_1.shape[1]):
            if m_1[i, j] != m_2[i, j]:
                compar = False
            break
        else:
            compar = True
    return compar


matritsa_1 = numpy.array([(54, 61, 37, 14), (17, 84, 63, 44), (14, 27, 11, 71), (64, 47, 79, 41)])
print(f'matritsa_1 = \n{matritsa_1}')
matritsa_2 = numpy.array([(38, 7, 12, 34), (46, 64, 23, 41), (58, 87, 21, 22), (20, 30, 0, 40)])
print(f'matritsa_2 = \n{matritsa_2}')

print()
print(f'Транспонированная матрица matritsa_1 = \n{matritsa_1.transpose()}')

print('\nПроверка коммутативности сложения матриц.')
matritsa_3 = matritsa_2 + matritsa_1
print(f'matritsa_3 = matritsa_2 + matritsa_1 = \n{matritsa_3}')
matritsa_4 = matritsa_1 + matritsa_2
print(f'matritsa_4 = matritsa_1 + matritsa_2 = \n{matritsa_4}')
compar1_res = matrix_comparer(matritsa_3, matritsa_4)
if compar1_res:
    print(f'Матрица matritsa_3 не отличается от матрицы matritsa_4.')
else:
    print(f'Матрица matritsa_3 отличается от матрицы matritsa_4.')

# Умножение матриц.
matritsa_5 = matritsa_2 @ matritsa_1
matritsa_6 = matritsa_2.dot(matritsa_1)
matritsa_7 = matritsa_1.dot(matritsa_2)

print('\nСравнение результатов умножения матриц с помощью оператора @ и посредством метода dot.')
compar1_res = matrix_comparer(matritsa_5, matritsa_6)
if compar1_res:
    print(f'Матрица matritsa_5 не отличается от матрицы matritsa_6.')
else:
    print(f'Матрица matritsa_5 отличается от матрицы matritsa_6.')

print('\nПроверка коммутативности умножения матриц.')
compar1_res = matrix_comparer(matritsa_6, matritsa_7)
if compar1_res:
    print(f'Матрица matritsa_6 не отличается от матрицы matritsa_7.')
else:
    print(f'Матрица matritsa_6 отличается от матрицы matritsa_7.')

sleep(4.0)
print()
# Работа с библиотекой requests.
print('Работа с библиотекой requests.')
req = requests.get('https://mail.ru/')
print(req)
if req == 200:
    print('Запрос прошёл успешно.')
else:
    print('Запрос прошёл неуспешно.')

print(req.headers)
print(req.text)
print(req.content)

sleep(4.0)
print()
# Работа с библиотекой Matplotlib.
print('Работа с библиотекой Matplotlib.')


def simpe_exponent_graph_creator(x_low_limit, x_up_limit, x_step):
    exp_fig, ax = matplotlib.pyplot.subplots(figsize=(10, 20))
    if (x_up_limit > 3.5 or x_low_limit < -10.0
        or x_step >= (x_up_limit - x_low_limit) / 2 or x_low_limit >= x_up_limit) or x_step <= 0:
        print('Функции simpe_exponent_graph_creator переданы недопустимые значения аргументов. '
              'Передайте корректные значения.')
        exit()

    x = numpy.arange(x_low_limit, x_up_limit, x_step)
    y = numpy.exp(x)
    line, = ax.plot(x, y, color='orange', lw=6, label='Экспонента')

    ax.annotate('Конец!', xy=(x_up_limit, numpy.exp(x_up_limit)),
                xytext=(2 * x_up_limit / 3 + x_low_limit / 3, numpy.exp(x_up_limit)),
                arrowprops=dict(facecolor='green', shrink=0.03))
    ax.annotate('Начало.', xy=(x_low_limit, numpy.exp(x_low_limit)),
                xytext=(x_up_limit / 3 + 2 * (x_low_limit) / 3, numpy.exp(0.8 * x_up_limit)),
                arrowprops=dict(facecolor='red', shrink=0.03))

    ax.set_ylim(0, 40)

    matplotlib.pyplot.xlabel('X')
    matplotlib.pyplot.ylabel('Y')
    matplotlib.pyplot.title('График экспоненты')
    matplotlib.pyplot.legend()


fig_1 = simpe_exponent_graph_creator(-3.0, 3.0, 0.01)
matplotlib.pyplot.savefig('fig_1.jpeg')
matplotlib.pyplot.show()
fig_2 = simpe_exponent_graph_creator(-6.0, 3.5, 0.01)
matplotlib.pyplot.savefig('fig_2.jpeg')
matplotlib.pyplot.show()

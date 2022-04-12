"""
Контрольная работа №6
Тема 1: “Модули и пакеты. Установка, обновление и удаление”
	•	Установите сторонний модуль texttable (https://pypi.org/project/texttable/).
	•	Выведите на экран справку о модуле texttable и его содержимое. Самостоятельно ознакомьтесь с возможностями
данного модуля.
	•	Выведите на экран значения специальных и дополнительных атрибутов модуля texttable. Какие из атрибутов
определены у модуля, а какие нет?
	•	Попробуйте обновить установленный модуль texttable.
	•	Удалите модуль texttable. Убедитесь, что модуль был удален и не может больше использоваться.
"""
import texttable

print(texttable.__doc__)
print(texttable.__file__)
print(texttable.__author__)
print(texttable.__credits__)
print(texttable.__license__)
print(texttable.__version__)

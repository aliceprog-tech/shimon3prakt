import re

text = """
Регулярные выражения представляют собой похожий, но гораздо более сильный инструмент
для поиска строк, проверки их на соответствие какому-либо шаблону и другой подобной
работы. Англоязычное название этого инструмента — Regular Expressions или просто RegExp.
Строго говоря, регулярные выражения — специальный язык для описания шаблонов строк.

AAAA aaaa AaAaAaAa 123 123 12345 11223344
A1Б2В3 АА11 ББ22ВВ 33ГГ44

Тест! --- Ещё! --- Даёшь! --- ЁЁЁёёё

QwertyЙцукен

+-,/[](),.***-(**), a*(b+[c+d])*e/f+g-h

!!!!""''####$$$$%%%%&&&''''(((()))***++++,,,,,,,,...////::::;;;;<<<<====>>>>????
@@@@[[[[\\\\]]]]]]^^^___```{{{{||||}}}}~~~~

<a href="#10">10: CamelCase -> under_score</a>;
<a href="#11">11: Удаление повторов</a>;
<a href="#12">12: Близкие слова</a>;

<a href="#13">13: Форматирование больших чисел</a>;
<a href="#14">14: Разделить текст на предложения</a>;
<a href="#15">15: Форматирование номера телефона</a>;
<a href="#16">16: Поиск e-mail'ов - 2</a>;
"""

print("=" * 60)
print("1. Натуральные числа")
print(re.findall(r'\b\d+\b', text))

print("=" * 60)
print("2. Слова, написанные капсом")
print(re.findall(r'\b[А-ЯA-ZЁ]+\b', text))

print("=" * 60)
print("3. Слова, где русская буква и затем цифра")
print(re.findall(r'\b[А-Яа-яЁё]+\d+\w*\b', text))

print("=" * 60)
print("4. Слова, начинающиеся с большой буквы")
print(re.findall(r'\b[A-ZА-ЯЁ][a-zа-яёA-ZА-ЯЁ]*\b', text))

print("=" * 60)
print("5. Слова, начинающиеся на гласную")
print(re.findall(r'\b[AEIOUYАЕЁИОУЫЭЮЯaeiouyаеёиоуыэюя]\w*\b', text))

print("=" * 60)
print("6. Натуральные числа НЕ на границе слова")
print(re.findall(r'(?<=\w)\d+(?=\w)', text))

print("=" * 60)
print("7. Строки с символом * не в конце")
lines = text.splitlines()
for line in lines:
    if re.search(r'\*.+', line):
        print(line)

print("=" * 60)
print("8. Строки с открывающей и закрывающей скобкой")
for line in lines:
    if re.search(r'\(.*\)', line):
        print(line)

print("=" * 60)
print("9. Весь кусок оглавления вместе с тегами")
toc = re.findall(r'<a href="#\d+">.*?</a>;', text)
for item in toc:
    print(item)

print("=" * 60)
print("10. Только текстовая часть оглавления")
toc_text = re.findall(r'>(.*?)</a>', text)
for item in toc_text:
    print(item)

print("=" * 60)
print("11. Пустые строки")
empty_lines = re.findall(r'^\s*$', text, re.MULTILINE)
print(f"Количество пустых строк: {len(empty_lines)}")

print("=" * 60)
print("12. Все теги без содержимого")
tags = re.findall(r'</?[^>]+>', text)
print(tags)

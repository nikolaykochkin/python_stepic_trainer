import re

text = '''Функция {0}(ДатаНачала, ДатаОкончания, СтруктураФильтров)
	
	Организация = Неопределено;
	СтруктураФильтров.Свойство("Организация", Организация);
	//Перечисления.itilprofПриоритеты.{1}
	Возврат ;

КонецФункции // {0}()'''

text2 = '''Метрики.Вставить("НеРешенныеТОСтандартные", НеРешенныеТОСтандартные");
Метрики.Вставить("НеРешенныеТОВысокие", "НеРешенныеТОВысокие");
Метрики.Вставить("НеРешенныеТОКритические", "НеРешенныеТОКритические");
Метрики.Вставить("НеРешенныеРемонтыСтандартные", "НеРешенныеРемонтыСтандартные");
Метрики.Вставить("НеРешенныеРемонтыВысокие", "НеРешенныеРемонтыВысокие");
Метрики.Вставить("НеРешенныеРемонтыКритические", "НеРешенныеРемонтыКритические");
Метрики.Вставить("ПросроченныеСтандартные", "ПросроченныеСтандартные");
Метрики.Вставить("ПросроченныеВысокие", "ПросроченныеВысокие");
Метрики.Вставить("ПросроченныеКритические", "ПросроченныеКритические");
Метрики.Вставить("ПриостановленныеСтандартные", "ПриостановленныеСтандартные");
Метрики.Вставить("ПриостановленныеВысокие", "ПриостановленныеВысокие");
Метрики.Вставить("ПриостановленныеКритические", "ПриостановленныеКритические");
Метрики.Вставить("РешенныеЧерезПриостановкуСтандартные", "РешенныеЧерезПриостановкуСтандартные");
Метрики.Вставить("РешенныеЧерезПриостановкуКритические", "РешенныеЧерезПриостановкуКритические");
Метрики.Вставить("РешенныеЧерезПриостановкуВысокие", "РешенныеЧерезПриостановкуВысокие");
Метрики.Вставить("ПросроченныеВсегоСтандартные", "ПросроченныеВсегоСтандартные");
Метрики.Вставить("ПросроченныеВсегоВысокие", "ПросроченныеВсегоВысокие");
Метрики.Вставить("ПросроченныеВсегоКритические", "ПросроченныеВсегоКритические");
Метрики.Вставить("ПереоткрытыеСтандартные", "ПереоткрытыеСтандартные");
Метрики.Вставить("ПереоткрытыеВысокие", "ПереоткрытыеВысокие");
Метрики.Вставить("ПереоткрытыеКритические", "ПереоткрытыеКритические");
Метрики.Вставить("НовыеСтандартные", "НовыеСтандартные");
Метрики.Вставить("НовыеВысокие", "НовыеВысокие");
Метрики.Вставить("НовыеКритические", "НовыеКритические");
'''

text2 = re.sub(r'(Метрики\.Вставить\("[а-яА-Я]+",\s)+', '', text2)
lst = text2.replace('");\n', '').split('"')
prior = ''
for line in lst:
    if line.find('Стандартные') > 0:
        prior = 'Средний'
    elif line.find('Высокие') > 0:
        prior = 'Высокий'
    else:
        prior = 'Критический'
    print(text.format(line, prior))
    print()
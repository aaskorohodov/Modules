'''
LIKE оператор сравнения.

Использует 2 регулярных выражения:
_       Любой единичный символ
%       Любая последовательность символов

Примеры:

SELECT * FROM table WHERE city_name LIKE '%z'
*будут выбраны city_name заканчивающиеся на z\

WHERE city_name LIKE '%burg'
*заканчивающиеся на burg

WHERE word LIKE 'hell_'
*все слова начинающиеся на hell и имеющие еще 1 символ

WHERE word LIKE '% % %'
*все значения из трех слов (hello my name)


Для экранирования используется ESCAPE:
LIKE '25|%' ESCAPE '|' – найдет строки содержащие "25%"


LIKE поддерживает NOT (NOT LIKE)


'''
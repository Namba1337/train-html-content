# Создаем HTML-страницу с информацией об организации
html_content = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Практическая подготовка</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .info {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Наименование организации на базе, которой Вы проходите практическую подготовку</h1>
    
    <div class="info">
        <h2>Об организации</h2>
        <p>«Об организации...»</p>
        <p>Здесь будет размещена подробная информация об организации, включая её историю, основные направления деятельности, контакты и другую важную информацию для практикантов.</p>
    </div>
</body>
</html>
'''

# Сохраняем HTML в файл
with open('organization_info.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML-страница успешно создана!")
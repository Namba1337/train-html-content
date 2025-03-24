html_content = '''
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <title>Университет Синергия</title>
  <style>
    /* Сброс базовых отступов */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Raleway, sans-serif;
      color: #0C143B;
      background-color: #ffffff;
    }

    /* Шапка сайта */
    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 20px 40px;
    }

    .logo img {
      height: 40px;
    }

    /* Навигация */
    nav ul {
      list-style: none;
      display: flex;
      gap: 20px;
    }

    nav ul li a {
      text-decoration: none;
      color: #0C143B;
      font-weight: 600;
    }

    nav ul li a:hover {
      color: #fe334a; 
      text-decoration: none;
    }

    /* Основной блок с заголовком и формой */
    .hero {
      padding: 60px 40px;
      position: relative;
      /* Светлый фон для контента */
      background-color: #f8f8f8;
    }

    .hero h1 {
      font-size: 64px;
      line-height: 1.2;
      font-weight: 600;
      margin-bottom: 20px;
      color: #0C143B;
    }

    .hero p {
      font-size: 24px;
      margin-bottom: 30px;
      max-width: 800px;
    }

    .br-red {
        color: #fe334a; 
    }

    /* Контейнер для формы */
    .form-container {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .form-container input {
      flex: 1 1 60%;
      min-width: 200px;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .form-container button {
      flex: 1 1 auto;
      background-color: #e10000; /* красная кнопка */
      color: #ffffff;
      border: none;
      padding: 10px 20px;
      font-size: 16px;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    .form-container button:hover {
      background-color: #c40000; /* затемнение при наведении */
    }

    .arrow-right {
      position: absolute;
      top: 50%;
      right: 40px;
      transform: translateY(-100%) scale(3);
      width: 60px; 
      height: 60px;
      object-fit: contain; /* Для сохранения пропорций */
    }

    .arrow-right path {
      stroke: currentColor; /* Наследование цвета из CSS */
    }

    @media (max-width: 768px) {
      header {
        flex-direction: column;
        gap: 20px;
      }

      nav ul {
        flex-wrap: wrap;
        justify-content: center;
      }

      .hero {
        padding: 40px 20px;
      }

      .hero h1 {
        font-size: 32px;
      }

      .form-container {
        flex-direction: column;
      }

      .arrow-right {
        display: none;
      }
    }
  </style>
</head>
<body>

  <header>
    <div class="logo">
      <img src="logo-fd06320174.svg" alt="Университет Синергия">
    </div>
    <nav>
      <ul>
        <li><a href="#">Колледж</a></li>
        <li><a href="#">Бакалавриат</a></li>
        <li><a href="#">Магистратура</a></li>
        <li><a href="#">Второе высшее</a></li>
        <li><a href="#">Аспирантура</a></li>
        <li><a href="#">MBA</a></li>
        <li><a href="#">Курсы</a></li>
      </ul>
    </nav>
  </header>

  <section class="hero">
    <!-- Пример дополнительного элемента-стрелки справа -->
    <img class="arrow-right" src="/arrow-dc3b5c12ab.svg" alt="Стрелка">

    <h1>Университет Синергия<br><span class="br-red">Приёмная комиссия</span><br>Поступи прямо сейчас!</h1>
    <p>Узнай минимальный проходной балл в 2025 году, оставь заявку</p>
'''

with open('admission_form.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Страница приёмной комиссии создана!")
<!DOCTYPE html>
{% load staticfiles %}
<html>
<head>
    <meta charset="utf-8">
    <title>
        {% block title %}
            {{ title|title }}
        {% endblock %}
    </title>
    {% block css %}
        <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
        <link rel="stylesheet" href="{% static 'fonts/font-awesome/css/font-awesome.css' %}">
    {% endblock %}
    {% block js %}
    {% endblock %}
</head>
<body>
<div class="basket_container">
    <div class="h2 text-center head">
        Ваша корзина,
        {% if user.first_name %}
            {{ user.first_name|title}}
        {% else %}
            {{ username }}
       {% endif %}
    </div>
    {% block content %}
    {% endblock %}
</div>
</body>
</html>


{% extends 'basketapp/base.html' %}

{% load static %}
{% block content %}
    <div class="basket_list">
        {% for item in basket_items %}
            <div class="basket_record">
                <img src="/media/{{ item.product.image }}"
                     alt="{{ item.product.short_desc }}">
                <span class="category_name">{{ item.product.category.name }}</span>
                <span class="product_name">{{ item.product.name }}</span>
                <span class="product_price">{{ item.product.price }}&nbspруб</span>
                <input type="number" name="{{ item.pk }}" min="0" value="{{ item.quantity }}">
                <span class="product_cost">{{ item.product_cost }}&nbspруб</span>
                <button class="btn btn-round">
                    <a href="{% url 'basket:remove' item.pk %}" class="">
                        удалить
                    </a>
                </button>
            </div>
        {% endfor %}
        {% if basket_items %}
            <div class="basket_summary">
                В корзине {{ basket_items.0.total_quantity }} товаров общей стоимостью
                {{ basket_items.0.total_cost }} руб
            </div>
        {% endif %}
        <button class="btn btn-round">
            <a href="{% url 'index' %}">на главную</a>
        </button>
    </div>
{% endblock %}
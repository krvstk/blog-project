# blog-project
My first real-programming practice using Django environment aimed of obtaining entry-level coding skills.

Back-end part is based on "Try Django 1.9" Guide by CodingEntrepreneurs. 

ss


{% extends "base.html" %}
{% load get_at_index %}

{% block head_title %}
{{ title }} | {{ block.super }}
{% endblock head_title %}



{{ instance.title }} | {{ block.super }}

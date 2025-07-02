---
layout: archive
title: "📚 Teaching"
title_tag: "Teaching"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}


Misc
------
<ul>
  {% assign misc_items = site.teaching_misc | sort: "date" | reverse %}
  {% for item in misc_items %}
    <li>
      <strong>{{ item.title }}</strong><br />
      <span style="font-size: 0.8em;">{{ item.description | markdownify | remove: '<p>' | remove: '</p>' | strip }}, {{ item.venue }}, {{ item.semester }}</span><br />
      {% if item.resources %}
        <span style="font-size: 0.8em;">
          {% for res in item.resources %}
            <a href="{{ res.url }}" target="_blank">{{ res.label }}</a>{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        </span>
      {% endif %}
    </li>
  {% endfor %}
</ul>
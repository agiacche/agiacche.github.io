---
layout: archive
title: "📚 Teaching"
title_tag: "Teaching"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

{% assign sorted_courses = site.teaching | sort: 'date' | reverse %}
{% for post in sorted_courses %}
  {% include archive-single.html %}
{% endfor %}

## Misc

<ul class="cv-list cv-list--compact">
  {% assign misc_items = site.teaching_misc | sort: "date" | reverse %}
  {% for item in misc_items %}
    <li class="cv-entry cv-entry--compact">
      <span class="cv-entry__dates">{{ item.semester }}</span>
      <span class="cv-entry__body">
        <span class="cv-entry__title">{{ item.title }}</span>
        {% if item.description %} &ndash; {{ item.description | markdownify | remove: '<p>' | remove: '</p>' | strip }}{% endif %}
        , {{ item.venue }}
        {% if item.resources %}
          <span class="pub-links">
            {% for res in item.resources %}
              <a class="pub-link" href="{{ res.url }}" target="_blank" rel="noopener noreferrer">
                <i class="fa-regular fa-file-pdf" aria-hidden="true"></i><span>{{ res.label }}</span>
              </a>
            {% endfor %}
          </span>
        {% endif %}
      </span>
    </li>
  {% endfor %}
</ul>
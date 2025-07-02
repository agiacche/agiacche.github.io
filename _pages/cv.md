---
layout: archive
title: "👨🏻‍🎓 CV"
title_tag: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
{% include toc %}

<div style="margin-top: 2em;"></div>

The [CV](http://agiacche.github.io/files/giacchetto_cv_en.pdf) can be downloaded here. Below is a brief summary.

Employment
------
* Oct 2023–present: 
  * ETH Fellow & Hermann-Weyl-Instructor, ETHZ
  * Mentor: Rahul Pandharipande
* Oct 2021–Oct 2023
  * Postdoctoral Fellow, IPhT
  * Mentor: Bertrand Eynard

Education
------
* **PhD** in Mathematics, MPIM, 2021
  * *[Geometric and topological recursion and invariants of the moduli space of curves](http://agiacche.github.io/files/ThesisPhD.pdf)*
  * Supervisor: Gaëtan Borot
* **MSc** in Mathematics, University of Trieste & SISSA, 2017
  * *[The J-equation on Kähler manifolds and blowups](http://agiacche.github.io/files/ThesisMSc.pdf)*
  * Supervisor: Jacopo Stoppa
* **BSc** in Mathematics, University of Trieste, 2015
  * *[Skein relations and polynomial invariants of knots and links](http://agiacche.github.io/files/ThesisBSc.pdf)*
  * Supervisor: Bruno Zimmermann

Publications and preprints
------
<ul>
  {% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
  {% for pub in sorted_pubs %}
    <li>
      <em>{{ pub.title | markdownify | remove: '<p>' | remove: '</p>' }}</em><br />
      <span style="font-size: 0.8em;">
        {% if pub.coauthors %}
          with {{ pub.coauthors }}.
        {% endif %}
        [
        <a href="https://arxiv.org/abs/{{ pub.arxiv }}" target="_blank" rel="noopener">arXiv</a>
        {% if pub.category == "published" or pub.category == "book" %}
          {% if pub.journal %}
            {% if pub.doi %}
              {% assign pub_link = "https://doi.org/" | append: pub.doi %}
            {% elsif pub.open %}
              {% assign pub_link = pub.open %}
            {% else %}
              {% assign pub_link = "https://arxiv.org/abs/" | append: pub.arxiv %}
            {% endif %}
            | <a href="{{ pub_link }}" target="_blank" rel="noopener">{{ pub.journal }}</a>
          {% endif %}
        {% endif %}
        ]
      </span>
    </li>
  {% endfor %}
</ul>
  
Teaching
------
<ul>
  {% assign combined_teaching = site.teaching | concat: site.teaching_misc %}
  {% assign sorted_teaching = combined_teaching | sort: 'date' | reverse %}
  
  {% for item in sorted_teaching %}
    <li>
      {% if item.permalink %}
        <em><a href="{{ item.permalink }}">{{ item.title }}</a></em>,
      {% else %}
        <em>{{ item.title }}</em>,
      {% endif %}
      {% if item.role %}{{ item.role }}, {% endif %}
      {% if item.venue %}{{ item.venue }}, {% endif %}
      {% if item.semester %}{{ item.semester }}{% endif %}
    </li>
  {% endfor %}
</ul>
  
Organization of events
------
<ul>
  {% assign sorted_events = site.events | sort: 'date' | reverse %}
  {% for event in sorted_events %}
    <li>
      {{ event.type }} 
      <em><a href="{{ event.link }}">{{ event.title }}</a></em>, 
      {{ event.venue }} ({{ event.when }})
    </li>
  {% endfor %}
</ul>

<!--
Research stays
------
* 2024 – University of Edinburgh, University of Tokyo, University of Science and Technology of China
* 2023 – University of Trieste
* 2022 – University of Geneva, SISSA, Leiden University, Humboldt University, University of Trieste
* 2021 – Humboldt University
* 2020 – University of Melbourne
* 2019 – Centre for Quantum Mathematics
-->

Honours
------
* ETH Fellowship: Oct 2023–Sep 2025
<!-- * Oberwolfach Leibniz Graduate Students 2021 -->
* Marco Reni prize 2018
<!-- * Friulovest Bank award 2017 -->
* SISSA MSc Fellowship: Sep 2015–Sep 2017
<!-- * Friulovest Bank award 2015 -->
* Best freshman, University of Trieste, 2012/13
* Luciano Fonda BSc Fellowship: Sep 2012–Sep 2015
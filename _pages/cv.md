---
layout: archive
title: "👨🏻‍🎓 CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

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
  * *[Geometric and topological recursion and invariants of the moduli space of curves](http://agiacche.github.io/files/PhDThesis.pdf)*
  * Supervisor: Gaëtan Borot
* **MSc** in Mathematics, University of Trieste & SISSA, 2017
  * *[The J-equation on Kähler manifolds and blowups](http://agiacche.github.io/files/MScThesis.pdf)*
  * Supervisor: Jacopo Stoppa
* **BSc** in Mathematics, University of Trieste, 2015
  * *[Skein relations and polynomial invariants of knots and links](http://agiacche.github.io/files/BScThesis.pdf)*
  * Supervisor: Bruno Zimmermann

Publications and preprints
------
<ul>
  {% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
  {% for pub in sorted_pubs %}
    <li>
      <em>{{ pub.title }}</em><br />
      {% if pub.coauthors %}
        {{ pub.coauthors }}. 
      {% endif %}
      <span style="font-size: 0.8em;">
        [
        <a href="https://arxiv.org/abs/{{ pub.arxiv }}" target="_blank" rel="noopener">arXiv</a>
        {% if pub.category == "published" or pub.category == "book" %}
          {% if pub.journal %}
            | <a href="{% if pub.doi and pub.doi != '0000' %}https://doi.org/{{ pub.doi }}{% else %}# {% endif %}" target="_blank" rel="noopener">
              {{ pub.journal }}
            </a>
          {% endif %}
        {% endif %}
        ]
      </span>
    </li>
  {% endfor %}
</ul>


Teaching
------
* [Toric geometry](https://agiacche.github.io/teaching/2025-spring-ToricGeometry), lecturer, Sping 2025, ETHZ
* [Riemann surfaces](https://agiacche.github.io/teaching/2024-spring-RiemannSurfaces), lecturer, Sping 2024, ETHZ
* Topology, teaching assistant, Spring 2017, UniTS
* Linear algebra, teaching assistant, Fall 2016, UniTS

Organization of events
------
* Workshop [Refinement in Enumerative Geometry and Physics](https://www.icts.res.in/current-and-upcoming-events), Bangalore (22 Jun–3 Jul, 2026)
* School [Quantum Geometry](https://houches24.github.io), Les Houches (29 July–23 Aug, 2024)
* School [Topological recursion and integrability](https://indico.in2p3.fr/event/29404), Trieste (11–16 Sep, 2023)
* Conference [Moduli spaces: theory and coding](https://indico.in2p3.fr/event/28594), Les Diablerets (27 Feb–3 Mar, 2023)
* School + workshop [TR Salento 2022](https://sites.google.com/view/tr-salento-2022/home), Otranto (5–16 Sep, 2022)
* Conference [Recent advances on moduli spaces of curves](https://sites.google.com/view/moduli2022/home), Leysin (18–24 March, 2022)
* On-line reading group [Donaldson–Thomas invariants](https://www.mathematik.hu-berlin.de/de/forschung/forschungsgebiete/mathematische-physik/borot-mp-homepage/online-reading-group-stability-conditions-and-dt-invariants), MPIM (Spring 2020)
* Reading group [Integer points in polyhedra](https://sites.google.com/view/integerpointsonpolyhedra/home), MPIM (Fall 2019)
* Reading group [Geometric recursion](https://sites.google.com/view/grlearningseminar/home), MPIM (Fall 2018)

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
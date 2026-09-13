---
title: "About me"
permalink: /
author_profile: true
---

I am **Boqiao Li (李泊桥)**, based at **Beihang University**. My research interests are **large language models**, **vision-language models**, and **autonomous driving**.

This is my academic homepage. I also keep a [blog](/blog/) with research notes, paper readings, coursework, and personal writing.

<p class="profile-links"><a href="mailto:liboqiao2004@gmail.com">Email</a><span aria-hidden="true"> / </span><a href="https://github.com/liboqiao1234">GitHub</a><span aria-hidden="true"> / </span><a href="https://www.linkedin.com/in/boqiao-li/">LinkedIn</a></p>

<h2 id="research">Research interests</h2>

- **Large language models** — language modeling and memory for language agents.
- **Vision-language models** — multimodal learning and understanding.
- **Autonomous driving** — learning and perception for autonomous systems.

{% if site.data.publications.size > 0 %}
## Publications
{% for paper in site.data.publications %}
<div class="research-entry"><h3>{% if paper.url %}<a href="{{ paper.url }}">{{ paper.title }}</a>{% else %}{{ paper.title }}{% endif %}</h3><p>{{ paper.authors }}<br><em>{{ paper.venue }}</em>{% if paper.year %}, {{ paper.year }}{% endif %}</p></div>
{% endfor %}
{% endif %}

{% if site.data.projects.size > 0 %}
## Projects
{% for project in site.data.projects %}
<div class="research-entry"><h3><a href="{{ project.url }}">{{ project.title }}</a></h3><p>{{ project.description }}</p></div>
{% endfor %}
{% endif %}

## Selected writing

<ul class="selected-writing">
{% assign featured = "Memory-for-LLM|【论文阅读】Memory-for-LLMs-综述|OO-Unit1-总结博客" | split: "|" %}
{% for slug in featured %}
{% assign target_url = slug | prepend: "/" | append: "/" %}
{% for post in site.data.legacy_posts %}{% if post.url == target_url %}
<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><time datetime="{{ post.date }}">{{ post.date | date: "%b %Y" }}</time></li>
{% endif %}{% endfor %}
{% endfor %}
</ul>

[All blog posts →](/blog/)

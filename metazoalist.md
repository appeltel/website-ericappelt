---
layout: default
title: Metazoa
subtitle: Mostly birds
category: metazoa
---

<div class="col-xs-12 col-md-12 blogpost" markdown="1"> 

The full list of animals that I have digitally captured and posted:

{% strip %}
{% for post in site.categories[page.category] %}
* [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }} ({{post.mclass}})
{% endfor %}
{% endstrip %}

</div>

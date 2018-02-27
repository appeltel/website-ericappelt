---
layout: default
title: Writing
subtitle: Mostly technical stuff
category: writing
---

<div class="col-xs-12 col-md-12 bigfont-column" markdown="1"> 

Things I have written:

{% for post in site.categories[page.category] %}
* [{{ post.title}}]({{ post.url }})
{% endfor %}

</div>

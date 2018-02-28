---
layout: default
title: Metazoa
subtitle: Mostly birds
category: metazoa
---

<div class="col-xs-12 col-md-12 blogpost" markdown="1"> 

Metazoans that I have digitally captured:

{% for post in site.categories[page.category] %}* [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }} ({{post.mclass}})
{% endfor %}

Unless otherwise specified, these are all wild animals that were
not baited in any manner.

</div>

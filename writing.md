---
layout: default
title: Writing
subtitle: Mostly technical stuff
category: writing
---

<div class="col-xs-12 col-md-12 blogpost" markdown="1"> 

Things I have written:

{% for post in site.categories[page.category] %}* {{ post.date | date: "%B %d, %Y" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

</div>

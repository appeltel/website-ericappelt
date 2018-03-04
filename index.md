---
layout: default
title: Eric Appelt
subtitle: Software, Science, and Stuff
---

<div class="col-xs-12 col-md-6 bigfont-column"> 
  <p id="randm"></p>
</div>
<script>
  var metazoa_string = "{{site.data["metazoa"] | join: ',' }}";
  var metazoa = metazoa_string.split(',');
  var mrand = metazoa[Math.floor(Math.random() * metazoa.length)];
  var elem = document.createElement("img");
  elem.src = mrand;
  elem.setAttribute("alt", "random metazoan");
  elem.setAttribute("class", "img-responsive center-block framed-image");
  document.getElementById("randm").appendChild(elem);
</script>

<div class="col-xs-12 col-md-6 bigfont-column" markdown="1"> 

### A collection of photos and writing

My wildlife photography, general and technical writing, and
professional contact information. I recommend the photography
part.

<a href="/metazoa.html" class="btn btn-block btn-primary bigfont">
Wildlife photography
</a>
<a href="/writing.html" class="btn btn-block btn-primary bigfont">
General and technical writing
</a>
<a href="/about.html" class="btn btn-block btn-primary bigfont">
About Me
</a>

</div>

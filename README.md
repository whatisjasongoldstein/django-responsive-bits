Django Responsive Bits
======================

The earlier beginnings of a responsive utility belt. I'll add things as I need 
them/have time to break them out of my other sites.

I use this in production, but don't guarantee much of anything.

## Images

The [Picture element](http://responsiveimages.org/) looks at the size of the document to decide what to do.
(See CSS background images with media queries.) 

That's all well and good, but it seems like it would be better to examine the image itself,
so if your image is 300 pixels wide, you just know that you probably want the 300px thumbnail,
or something close to it.

You should probably use the picture element or srcset, but you find your layout hard to achieve in
these tools, the `image_sizes` may work.

### Setup:

Put `responsive_bits` in INSTALLED_APPS.

A newish version of jQuery is required.

### Usages:

Add `<script src="{{ STATIC_URL }}js/deferred-images.js">` in your base template.

    {% load thumanils responsive_tags %}
    
    {% thumbnail object.image 600x360 crop=",1" as small_img %}
    {% thumbnail object.image 1000x600 crop=",1" as medium_img %}
    {% thumbnail object.image 1200x720 crop=",1" as large_img %}
    {% thumbnail object.image 1600x960 crop=",1" as massive_img %}

    <img data-img-sizes={% image_sizes 1=small_img.url 900=medium_img.url 1200=large_img.url 1500=massive_img.url %} src="{{ small_img }}">

And that's it. You get the small version by default, the medium version if the image is at least 900px wide, etc.

Always go smallest to largest.

Setting `src` is optional, but if you don't your image will be blank without javascript, and people living in 1998 will laugh at you. You also risk a flash of empty image.

You can also support retina devices by adding `data-retina="true"` (or any value), and the image width used to decide which thumbnail to use will be multiplied by the device's pixel density. Use this wisely; just because I have a nice screen
doesn't mean the coffee shop wifi or 3G connection isn't going to wimper when you start throwing giant images at me.

#### Background Images

Of course, sometimes you might want to set a background-image on an element instead. Do this by setting the `data-as-bg` parameter.

    {% thumbnail object.image 200x100 crop=",1" as small_img %}
    {% thumbnail object.image 300x150 crop=",1" as medium_img %}
    {% thumbnail object.image 500x250 crop=",1" as large_img %}

    <div class="art" data-as-bg="1" data-img-sizes={% image_sizes 1=small_img.url 200=medium_img.url 400=large_img.url %} 
        style="background-image: {{ small_img }};"></div>

My examples use [Easy Thumbnails](https://github.com/SmileyChris/easy-thumbnails) (`pip install easy-thumbnails`), but virtually any library should be fine. The important part is that you can pass the thumbnail urls in as variables.



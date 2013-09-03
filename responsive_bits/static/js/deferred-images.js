
/* IMPROVED DEFER IMG
=====================
<img data-img-sizes="{&quot;50&quot;: &quot;small_thumb.jpg&quot;, &quot;500&quot;: &quot;medium.jpg&quot;, &quot;1000&quot;: &quot;big.jpg&quot; }">

This examines the image tag's width, and finds the nearest suitable thumbnail without going over.

*/
(function(){
    var images = $("[data-img-sizes]");
    images.each(function(i){
        var img = images[i];
        sizes = img.getAttribute('data-img-sizes');
        sizes = JSON.parse(sizes);
        var img_width = img.width;
        var new_src = img.src;
        var new_src_size = 0;
        for (key in sizes){
            key = parseInt(key, 10);
            if (key <= img_width && key > new_src_size){
                new_src = sizes[key];
                new_src_size = key;
            }
        }
        img.src = new_src;
    });
})();

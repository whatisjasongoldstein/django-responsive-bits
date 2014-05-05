
/* IMPROVED DEFER IMG
=====================
<img data-img-sizes="{&quot;50&quot;: &quot;small_thumb.jpg&quot;, &quot;500&quot;: 
&quot;medium.jpg&quot;, &quot;1000&quot;: &quot;big.jpg&quot; }">

This examines the image tag's width, and finds the nearest suitable thumbnail without going over.

To set the background-image instead of the src, set data-as-bg="1"

You can also set data-retina="1" if you want to show HD images for retina devices.

*/
(function(){

    var load_best_images = function(){
        var $images = $("[data-img-sizes]");
        _.each($images, function(img, i){
            sizes = img.getAttribute('data-img-sizes'); // Get JSON as a string.
            sizes = JSON.parse(sizes);
            var img_width = img.width || img.offsetWidth;

            // If data-retina is set, get images that are suitable for this pixel density as well
            if (window.devicePixelRatio !== undefined && img.getAttribute("data-retina")){
                img_width = img_width * window.devicePixelRatio;
            }

            var bgsrc;
            var new_src = img.src;
            var new_src_size = 0;
            for (key in sizes){
                key = parseInt(key, 10);
                if (key <= img_width && key > new_src_size){
                    new_src = sizes[key];
                    new_src_size = key;
                }
            }

            if (img.getAttribute("data-as-bg")) {
                bgsrc = "url(" + new_src + ")";
                if (window.getComputedStyle(img)["background-image"] !== bgsrc) {
                    img.style.setProperty("background-image", bgsrc);
                }
            } else {
                if (img.src !== new_src) {
                    img.src = new_src;
                }
            }
        });
    };

    load_best_images();
    $(window).on('resize orientationchange', _.debounce(load_best_images, 250));
    $(window).on("newcontent", load_best_images);

})();

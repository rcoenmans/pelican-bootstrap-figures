# Bootstap figures plugin for Pelican

A Pelican plugin that creates a [Bootstrap figure element](https://getbootstrap.com/docs/4.4/content/figures/) with figure caption (right aligned) out of images. The `alt` attribute of the `img` becomes the caption.

By default, Pelican will render any image using the img-tag.
```html
<img alt="This is an image of a starship destroyer" src="/starship_destroyer.png" />
```

With the pelican-bootstrap-figure plugin enabled, that same image will be rendered as a Bootstrap figure component with the caption aligned to the right.
```html
<figure class="figure">
    <img alt="This is an image of a starship destroyer" class="figure-img img-fluid" src="/starship_destroyer.png" />
    <figcaption class="figure-caption text-right">This is an image of a starship destroyer</figcaption>
</figure>
```

## Installation
```powershell
pip install pelican-bootstrap-figures
```

## Configuration
Enable the plugin in your `pelicanconf.py`.
```python
PLUGINS = [ 'pelican_bootstrap_figures' ]
```
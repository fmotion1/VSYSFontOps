# python-fontbro

Friendly font operations on top of `fontTools`.

## Usage

```python
from fontbro import Font
font = Font("fonts/MyFont.ttf")
```

## Methods

[`clone`](https://pypi.org/project/python-fontbro/#clone)

[`close`](https://pypi.org/project/python-fontbro/#close)

[`get_characters`](https://pypi.org/project/python-fontbro/#get_characters)

[`get_characters_count`](https://pypi.org/project/python-fontbro/#get_characters_count)

[`get_features`](https://pypi.org/project/python-fontbro/#get_features)

[`get_features_tags`](https://pypi.org/project/python-fontbro/#get_features_tags)

[`get_format`](https://pypi.org/project/python-fontbro/#get_format)

[`get_fingerprint`](https://pypi.org/project/python-fontbro/#get_fingerprint)

[`get_fingerprint_match`](https://pypi.org/project/python-fontbro/#get_fingerprint_match)

[`get_glyphs`](https://pypi.org/project/python-fontbro/#get_glyphs)

[`get_glyphs_count`](https://pypi.org/project/python-fontbro/#get_glyphs_count)

[`get_image`](https://pypi.org/project/python-fontbro/#get_image)

[`get_italic_angle`](https://pypi.org/project/python-fontbro/#get_italic_angle)

[`get_name`](https://pypi.org/project/python-fontbro/#get_name)

[`get_names`](https://pypi.org/project/python-fontbro/#get_names)

[`get_style_flag`](https://pypi.org/project/python-fontbro/#get_style_flag)

[`get_style_flags`](https://pypi.org/project/python-fontbro/#get_style_flags)

[`get_ttfont`](https://pypi.org/project/python-fontbro/#get_ttfont)

[`get_unicode_block_by_name`](https://pypi.org/project/python-fontbro/#get_unicode_block_by_name)

[`get_unicode_blocks`](https://pypi.org/project/python-fontbro/#get_unicode_blocks)

[`get_unicode_script_by_name`](https://pypi.org/project/python-fontbro/#get_unicode_script_by_name)

[`get_unicode_scripts`](https://pypi.org/project/python-fontbro/#get_unicode_scripts)

[`get_variable_axes`](https://pypi.org/project/python-fontbro/#get_variable_axes)

[`get_variable_axes_tags`](https://pypi.org/project/python-fontbro/#get_variable_axes_tags)

[`get_variable_axis_by_tag`](https://pypi.org/project/python-fontbro/#get_variable_axis_by_tag)

[`get_variable_instances`](https://pypi.org/project/python-fontbro/#get_variable_instances)

[`get_variable_instance_closest_to_coordinates`](https://pypi.org/project/python-fontbro/#get_variable_instance_closest_to_coordinates)

[`get_version`](https://pypi.org/project/python-fontbro/#get_version)

[`get_weight`](https://pypi.org/project/python-fontbro/#get_weight)

[`get_width`](https://pypi.org/project/python-fontbro/#get_width)

[`is_static`](https://pypi.org/project/python-fontbro/#is_static)

[`is_variable`](https://pypi.org/project/python-fontbro/#is_variable)

[`rename`](https://pypi.org/project/python-fontbro/#rename)

[`save`](https://pypi.org/project/python-fontbro/#save)

[`save_as_woff`](https://pypi.org/project/python-fontbro/#save_as_woff)

[`save_as_woff2`](https://pypi.org/project/python-fontbro/#save_as_woff2)

[`set_name`](https://pypi.org/project/python-fontbro/#set_name)

[`set_names`](https://pypi.org/project/python-fontbro/#set_names)

[`set_style_flag`](https://pypi.org/project/python-fontbro/#set_style_flag)

[`set_style_flags`](https://pypi.org/project/python-fontbro/#set_style_flags)

[`set_style_flags_by_subfamily_name`](https://pypi.org/project/python-fontbro/#set_style_flags_by_subfamily_name)

[`subset`](https://pypi.org/project/python-fontbro/#subset)

[`to_sliced_variable`](https://pypi.org/project/python-fontbro/#to_sliced_variable)

[`to_static`](https://pypi.org/project/python-fontbro/#to_static)

## Method Details

### clone

```python
"""
Creates a new Font instance reading the same binary file.
"""
font_clone = font.clone()
```

### close

```python
"""  
Close the wrapped TTFont instance.  
"""  
font.close()
```

### get\_characters

```python
"""  
Gets the font characters.

:param ignore\_blank: If True, characters without contours will not be returned.  
:type ignore\_blank: bool

:returns: The characters.  
:rtype: generator of dicts

:raises TypeError: If it's not possible to find the 'best' unicode cmap dict in the font.  
"""  
chars = font.get\_characters(ignore\_blank=False)
```

### get\_characters\_count

```python
"""  
Gets the font characters count.

:param ignore_blank: If True, characters without contours will not be counted.  
:type ignore_blank: bool

:returns: The characters count.  
:rtype: int  
"""  
chars_count = font.get_characters_count(ignore_blank=False)
```

### get\_features

```python
"""  
Gets the font opentype features.

:returns: The features.  
:rtype: list of dict  
"""  
features = font.get_features()
```

### get\_features\_tags

```python
"""  
Gets the font opentype features tags.

:returns: The features tags list.  
:rtype: list of str  
"""  
features_tags = font.get_features_tags()
```

### get\_fingerprint

```python
"""  
Gets the font fingerprint: an hash calculated from an image representation of the font.  
Changing the text option affects the returned fingerprint.

:param text: The text used for generating the fingerprint, default value: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".  
:type text: str  
:returns: The fingerprint hash.  
:rtype: imagehash.ImageHash  
"""  
hash = font.get_fingerprint()
```

### get\_fingerprint\_match

```python
"""  
Gets the fingerprint match between this font and another one.  
by checking if their fingerprints are equal (difference <= tolerance).

:param other: The other font, can be either a filepath or a Font instance.  
:type other: str or Font  
:param tolerance: The diff tolerance, default 3.  
:type tolerance: int  
:param text: The text used for generating the fingerprint, default value: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".  
:type text: str  
:returns: A tuple containing the match info (match, diff, hash, other_hash).  
:rtype: tuple  
"""  
match, diff, hash, other_hash = font.get_fingerprint_match(other="other_font.ttf", tolerance=10)
```

### get\_format

```python
"""  
Gets the font format: otf, ttf, woff, woff2.

:param ignore_flavor: If True, the original format without compression will be returned.  
:type ignore_flavor: bool

:returns: The format.  
:rtype: str or None  
"""  
format = font.get_format(ignore_flavor=False)
```

### get\_glyphs

```python
"""  
Gets the font glyphs and their own composition.

:returns: The glyphs.  
:rtype: generator of dicts  
"""  
glyphs = font.get_glyphs()
```

### get\_glyphs\_count

```python
"""  
Gets the font glyphs count.

:returns: The glyphs count.  
:rtype: int  
"""  
glyphs_count = font.get_glyphs_count()
```

### get\_image

```python
"""  
Gets an image representation of the font rendering  
some text using the given options.

:param text: The text rendered in the image  
:type text: str  
:param size: The font size  
:type size: int  
:param color: The text color  
:type color: tuple  
:param background\_color: The background color  
:type background\_color: tuple  
"""  
img = font.get\_image(text="Hello!", size=48, color=(0, 0, 0, 255), background\_color=(255, 255, 255, 255))
```

### get\_italic\_angle

```python
"""  
Gets the font italic angle.

:returns: The angle value including backslant, italic and roman flags.  
:rtype: dict or None  
"""  
italic\_angle = font.get\_italic\_angle()
```

### get\_name

```python
"""  
Gets the name by its identifier from the font name table.

:param key: The name id or key (eg. "family\_name")  
:type key: int or str

:returns: The name.  
:rtype: str or None

:raises KeyError: if the key is not a valid name key/id  
"""  
family\_name = font.get\_name(key=Font.NAME\_FAMILY\_NAME)
```

### get\_names

```python
"""  
Gets the names records mapped by their property name.

:returns: The names.  
:rtype: dict  
"""  
names = font.get\_names()
```

### get\_style\_flag

```python
"""  
Gets the style flag reading OS/2 and macStyle tables.

:param key: The key  
:type key: string

:returns: The style flag.  
:rtype: bool  
"""  
flag = font.get\_style\_flag(Font.STYLE\_FLAG\_BOLD)
```

### get\_style\_flags

```python
"""  
Gets the style flags reading OS/2 and macStyle tables.

:returns: The dict representing the style flags.  
:rtype: dict  
"""  
flags = font.get\_style\_flags()
```

### get\_ttfont

```python
"""  
Gets the wrapped TTFont instance.

:returns: The TTFont instance.  
:rtype: TTFont  
"""  
ttfont = font.get\_ttfont()
```

### get\_unicode\_block\_by\_name

```python
"""  
Gets the unicode block by name (name is case-insensitive and ignores "-").

:param name: The name  
:type name: str

:returns: The unicode block dict if the name is valid, None otherwise.  
:rtype: dict or None  
"""  
block = font.get\_unicode\_block\_by\_name(name="Basic Latin")
```

### get\_unicode\_blocks

```python
"""  
Gets the unicode blocks and their coverage.  
Only blocks with coverage >= coverage\_threshold (0.0 <= coverage\_threshold <= 1.0) will be returned.

:param coverage\_threshold: The minumum required coverage for a block to be returned.  
:type coverage\_threshold: float

:returns: The list of unicode blocks.  
:rtype: list of dicts  
"""  
blocks = font.get\_unicode\_blocks(coverage\_threshold=0.00001)
```

### get\_unicode\_script\_by\_name

```python
"""  
Gets the unicode script by name/tag (name/tag is case-insensitive and ignores "-").

:param name: The name  
:type name: str

:returns: The unicode script dict if the name/tag is valid, None otherwise.  
:rtype: dict or None  
"""  
script = font.get\_unicode\_script\_by\_name(name="Latn")
```

### get\_unicode\_scripts

```python
"""  
Gets the unicode scripts and their coverage.  
Only scripts with coverage >= coverage\_threshold (0.0 <= coverage\_threshold <= 1.0) will be returned.

:param coverage\_threshold: The minumum required coverage for a script to be returned.  
:type coverage\_threshold: float

:returns: The list of unicode scripts.  
:rtype: list of dicts  
"""  
scripts = font.get\_unicode\_scripts(coverage\_threshold=0.00001)
```

### get\_variable\_axes

```python
"""  
Gets the font variable axes.

:returns: The list of axes if the font is a variable font otherwise None.  
:rtype: list of dict or None  
"""  
axes = font.get\_variable\_axes()
```

### get\_variable\_axes\_tags

```python
"""  
Gets the variable axes tags.

:returns: The variable axis tags.  
:rtype: list or None  
"""  
axes\_tags = font.get\_variable\_axes\_tags()
```

### get\_variable\_axis\_by\_tag

```python
"""  
Gets a variable axis by tag.

:param tag: The tag  
:type tag: string

:returns: The variable axis by tag.  
:rtype: dict or None  
"""  
axis = font.get\_variable\_axis\_by\_tag(tag="wght")
```

### get\_variable\_instances

```python
"""  
Gets the variable instances.

:returns: The list of instances if the font is a variable font otherwise None.  
:rtype: list of dict or None  
"""  
instances = font.get\_variable\_instances()
```

### get\_variable\_instance\_closest\_to\_coordinates

```python
"""  
Gets the variable instance closest to coordinates.  
eg. coordinates = {"wght": 1000, "slnt": 815, "wdth": 775}

:param coordinates: The coordinates  
:type coordinates: dict

:returns: The variable instance closest to coordinates.  
:rtype: dict or None  
"""  
instance = font.get\_variable\_instance\_closest\_to\_coordinates(coordinates={"wght": 1000, "slnt": 815, "wdth": 775})
```

### get\_version

```python
"""  
Gets the font version.

:returns: The font version value.  
:rtype: float  
"""  
version = font.get\_version()
```

### get\_weight

```python
"""  
Gets the font weight value and name.

:returns: The weight name and value.  
:rtype: dict or None  
"""  
weight = font.get\_weight()
```

### get\_width

```python
"""  
Gets the font width value and name.

:returns: The width name and value.  
:rtype: dict or None  
"""  
width = font.get\_width()
```

### is\_static

```python
"""  
Determines if the font is a static font.

:returns: True if static font, False otherwise.  
:rtype: bool  
"""  
static = font.is\_static()
```

### is\_variable

```python
"""  
Determines if the font is a variable font.

:returns: True if variable font, False otherwise.  
:rtype: bool  
"""  
variable = font.is\_variable()
```

### rename

```python
"""  
Renames the font names records (1, 2, 4, 6, 16, 17) according to  
the given family\_name and style\_name (subfamily\_name).

If family\_name is not defined it will be auto-detected.  
If style\_name is not defined it will be auto-detected.

:param family\_name: The family name  
:type family\_name: str  
:param style\_name: The style name  
:type style\_name: str  
:param style\_flags: if True the style flags will be updated by subfamily name  
:type style\_flags: bool

:raises ValueError: if the computed PostScript-name is longer than 63 characters.  
"""  
font.rename(family\_name="My Font New", style\_name="Bold Italic")
```

### save

```python
"""  
Saves the font at filepath.

:param filepath: The filepath, if None the source filepath will be used  
:type filepath: str or None  
:param overwrite: The overwrite, if True the source font file can be overwritten  
:type overwrite: bool

:returns: The filepath where the font has been saved to.  
:rtype: str

:raises ValueError: If the filepath is the same of the source font and overwrite is not allowed.  
"""  
saved\_font\_path = font.save(filepath=None, overwrite=False)
```

### save\_as\_woff

```python
"""  
Saves font as woff.

:param filepath: The filepath  
:type filepath: str  
:param overwrite: The overwrite, if True the source font file can be overwritten  
:type overwrite: bool

:returns: The filepath where the font has been saved to.  
:rtype: str  
"""  
saved\_font\_path = font.save\_as\_woff(filepath=None, overwrite=True)
```

### save\_as\_woff2

```python
"""  
Saves font as woff2.

:param filepath: The filepath  
:type filepath: str  
:param overwrite: The overwrite, if True the source font file can be overwritten  
:type overwrite: bool

:returns: The filepath where the font has been saved to.  
:rtype: str  
"""  
saved\_font\_path = font.save\_as\_woff2(filepath=None, overwrite=True)
```

### set\_name

```python
"""  
Sets the name by its identifier in the font name table.

:param key: The name id or key (eg. "family\_name")  
:type key: int or str  
:param value: The value  
:type value: str  
"""  
font.set\_name(Font.NAME\_FAMILY\_NAME, "Family Name Renamed")
```

### set\_names

```python
"""  
Sets the names by their identifier in the name table.

:param names: The names  
:type names: dict  
"""  
font.set\_names(names={  
Font.NAME\_FAMILY\_NAME: "Family Name Renamed",  
Font.NAME\_SUBFAMILY\_NAME: "Regular Renamed",  
})
```

### set\_style\_flag

```python
"""  
Sets the style flag.

:param key: The flag key  
:type key: str  
:param value: The value  
:type value: bool  
"""  
font.set\_style\_flag(Font.STYLE\_FLAG\_BOLD, True)
```

### set\_style\_flags

```python
"""  
Sets the style flags, flags set to None will be ignored.

:param bold: The bold flag value.  
:type bold: bool or None  
:param italic: The italic flag value.  
:type italic: bool or None  
:param underline: The underline flag value.  
:type underline: bool or None  
:param outline: The outline flag value.  
:type outline: bool or None  
"""  
font.set\_style\_flags(regular=None, bold=None, italic=None, outline=None, underline=None)
```

### set\_style\_flags\_by\_subfamily\_name

```python
"""  
Sets the style flags by the subfamily name value.  
The subfamily values should be "regular", "italic", "bold" or "bold italic"  
to allow this method to work properly.  
"""  
font.set\_style\_flags\_by\_subfamily\_name()
```

### subset

```python
"""  
Subsets the font using the given options (unicodes or glyphs or text),  
it is possible to pass also subsetter options, more info here:  
https://github.com/fonttools/fonttools/blob/main/Lib/fontTools/subset/\_\_init\_\_.py

:param unicodes: The unicodes  
:type unicodes: str or list  
:param glyphs: The glyphs  
:type glyphs: list  
:param text: The text  
:type text: str  
:param options: The subsetter options  
:type options: dict  
"""  
font.subset(unicodes="", glyphs=\[\], text="", \*\*options)
```

### to\_sliced\_variable

```python
"""  
Converts the variable font to a partial one slicing the variable axes at the given coordinates.  
If an axis value is not specified, the axis will be left untouched.  
If an axis min and max values are equal, the axis will be pinned.

:param coordinates: The coordinates dictionary, each item value must be tuple/list/dict  
(with 'min', 'default' and 'max' keys) for slicing or float/int for pinning, eg.  
{'wdth':100, 'wght':(100,600), 'ital':(30,65,70)} or  
{'wdth':100, 'wght':\[100,600\], 'ital':\[30,65,70\]} or  
{'wdth':100, 'wght':{'min':100,'max':600}, 'ital':{'min':30,'default':65,'max':70}}  
:type coordinates: dict  
:param options: The options for the fontTools.varLib.instancer  
:type options: dictionary

:raises TypeError: If the font is not a variable font  
:raises ValueError: If the coordinates are not defined (empty)  
:raises ValueError: If the coordinates axes are all pinned  
"""  
font.to\_sliced\_variable(coordinates, \*\*options)
```

### to\_static

```python
"""  
Converts the variable font to a static one pinning the variable axes at the given coordinates.  
If an axis value is not specified, the axis will be pinned at its default value.  
If coordinates are not specified each axis will be pinned at its default value.

:param coordinates: The coordinates, eg. {"wght":500, "ital":50}  
:type coordinates: dict or None  
:param style\_name: The existing instance style name, eg. 'Black'  
:type style\_name: str or None  
:param options: The options for the fontTools.varLib.instancer  
:type options: dictionary

:raises TypeError: If the font is not a variable font  
:raises ValueError: If the coordinates axes are not all pinned  
"""  
font.to\_static(coordinates=None, \*\*options)
```

## Testing

```python
\# clone repository  
git clone https://github.com/fabiocaccamo/python-fontbro.git && cd python-fontbro

\# create virtualenv and activate it  
python -m venv venv && . venv/bin/activate

\# upgrade pip  
python -m pip install --upgrade pip

\# install requirements  
python -m pip install -r requirements.txt -r requirements-test.txt

\# install pre-commit to run formatters and linters  
pre-commit install --install-hooks

\# run tests using tox  
tox

\# or run tests using unittest  
python -m unittest
```
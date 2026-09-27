# beets-importopen

Adds an **Open folder** choice (key `o`) to the beets import prompt.

It opens the folder being imported in the file browser (`open` on macOS,
`xdg-open` on Linux), so you can look at the files before you decide. The
prompt is shown again afterwards. A multi-disc album opens every disc
folder.

## Install

Install it into the same Python environment as beets:

```sh
pip install git+https://github.com/dewey/beets-importopen
# or, in a uv project
uv add "beets-importopen @ git+https://github.com/dewey/beets-importopen"
```

Then enable it in your beets config:

```yaml
plugins: importopen
```

Requires beets 2.8 or newer.

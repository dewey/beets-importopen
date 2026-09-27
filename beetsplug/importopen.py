"""Beets plugin that adds "Open" to the import prompt.

Opens the folder being imported in the file browser (Finder on macOS), so
the files can be checked before deciding. For a single track it opens the
folder with that file selected. The prompt is shown again after.
"""

import os
import subprocess
import sys

from beets import ui
from beets.plugins import BeetsPlugin
from beets.util import PromptChoice, displayable_path, syspath


class ImportOpenPlugin(BeetsPlugin):
    def __init__(self):
        super().__init__()
        self.register_listener("before_choose_candidate", self.choices)

    def choices(self, session, task):
        return [PromptChoice("o", "Open folder", self.open)]

    def open(self, session, task):
        # A multi-disc album has one path per disc folder. In track mode the
        # path is the file itself, so show its folder instead of playing it.
        for path in task.paths:
            ui.print_(f"Opening {displayable_path(path)}")
            subprocess.run(open_command(syspath(path)), check=True)
        return None


def open_command(path):
    if sys.platform == "darwin":
        if os.path.isfile(path):
            # -R shows the file selected in its Finder folder.
            return ["open", "-R", path]
        return ["open", path]
    if os.path.isfile(path):
        path = os.path.dirname(path)
    return ["xdg-open", path]

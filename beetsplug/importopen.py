"""Beets plugin that adds "Open" to the import prompt.

Opens the folder being imported in the file browser (Finder on macOS), so
the files can be checked before deciding. The prompt is shown again after.
"""

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
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        # A multi-disc album has one path per disc folder.
        for path in task.paths:
            ui.print_(f"Opening {displayable_path(path)}")
            subprocess.run([opener, syspath(path)], check=True)
        return None

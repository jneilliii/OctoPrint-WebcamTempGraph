# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class WebcamTempGraph(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin):
	def on_after_startup(self):
			self._logger.info("WebcamTempGraph loaded!")

__plugin_name__ = "WebcamTempGraph"
__plugin_implementation__ = WebcamTempGraph()

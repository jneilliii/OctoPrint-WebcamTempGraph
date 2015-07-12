# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class WebcamTempGraph(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.SettingsPlugin):
	def on_after_startup(self):
		self._logger.info("WebcamTempGraph loaded!")
			
	def get_template_vars(self):
        return dict(webcamurl=self._settings.get(["webcam","stream"]))
			
__plugin_name__ = "WebcamTempGraph"
__plugin_implementation__ = WebcamTempGraph()

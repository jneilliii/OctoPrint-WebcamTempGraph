# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.settings

class WebcamTempGraph(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("WebcamTempGraph loaded!")
			
	def get_template_vars(self):
		return dict(webcamurl=octoprint.settings.settings().get(["webcam","stream"]))
		
	def get_assets(self):
		return dict(js=["js/webcamtempgraph.js"])
			
__plugin_name__ = "WebcamTempGraph"
__plugin_implementation__ = WebcamTempGraph()

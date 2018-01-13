# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class WebcamTempGraph(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("WebcamTempGraph loaded!")
			
	def get_template_vars(self):
		return dict(webcamurl=octoprint.settings.settings().get(["webcam","stream"]))
		
	def get_assets(self):
		return dict(js=["js/webcamtempgraph.js"])
		
    def get_update_information(self):
        return dict(
            webcamtab=dict(
                displayName="Webcam Tab",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="jneilliii",
                repo="OctoPrint-WebcamTempGraph",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/malnvenshorn/OctoPrint-WebcamTempGraph/archive/{target_version}.zip"
            )
        )
			
__plugin_name__ = "WebcamTempGraph"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = WebcamTempGraph()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

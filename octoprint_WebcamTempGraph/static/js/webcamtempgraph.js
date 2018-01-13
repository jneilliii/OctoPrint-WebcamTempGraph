/*
 * View model for OctoPrint-WebcamTab
 *
 * Author: Sven Lohrmann
 * License: AGPLv3
 */
$(function() {
    function WebcamTabViewModel(parameters) {
        var self = this;

        self.control = parameters[0];

        self.control.onTabChange = function (current, previous) {
            if (current == "#temp") {
                self.control._enableWebcam();
            } else if (previous == "#temp") {
                self.control._disableWebcam();
            }
        };

        self.onStartup = function() {
            $("#temp").append($("#webcam_container").detach());
        };
    };

    OCTOPRINT_VIEWMODELS.push({
        construct: WebcamTabViewModel,
        dependencies: ["controlViewModel"],
        elements: ["#temp"]
    });
});
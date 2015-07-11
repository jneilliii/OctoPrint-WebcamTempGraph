$(function () {
	function webcamtempgraphViewModel(parameters) {
		var self = this;

		self.onTabChange = function (current, previous) {
			if (current == "#temperature-graph") {
				$("div#temperature-graph").css("background-image","url("+$("img#webcam_image").attr("src")+")");
			}
		};
	}

	// This is how our plugin registers itself with the application, by adding some configuration information to
	// the global variable ADDITIONAL_VIEWMODELS
	ADDITIONAL_VIEWMODELS.push([
			// This is the constructor to call for instantiating the plugin
			webcamtempgraphViewModel,

			// This is a list of dependencies to inject into the plugin, the order which you request here is the order
			// in which the dependencies will be injected into your view model upon instantiation via the parameters
			// argument
			[],

			// Finally, this is the list of all elements we want this view model to be bound to.
			[("#temperature-graph")]
		]);
});

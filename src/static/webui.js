"use strict";

var WebUI = WebUI || {};

WebUI.initialize = function() {
    WebUI.getChannels().forEach(function(channel) {
	document.getElementById('channel-list')
	    .innerHTML += '<span class="channel">'+channel+'</span><br />';
    });
    
    console.log("initialized");
};

WebUI.getChannels = function() {
    return ['1064CBread', 'Other Conversation', 'Foobar'];
}

document.addEventListener('DOMContentLoaded', function() {
    WebUI.initialize();
});

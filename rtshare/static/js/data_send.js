$(document).ready(function() {
    var editor = CodeMirror.fromTextArea(document.getElementById('typed-text'), {
        lineNumbers: true,
        mode: "null",
        gutter: true,
        lineNumbers: true,
        styleSelectedText: true,
    });
    for (var i = 0; i < CodeMirror.modeInfo.length; i++) {
        var info = CodeMirror.modeInfo[i];
        $('#select-syntax').append($('<option>', {"value" : info.name }).text(info.name));
    }
    $('#select-syntax').on('change', function() {
        editor.setOption("mode", CodeMirror.findModeByName(this.value).mime);
    });
    const roomName = JSON.parse(document.getElementById('room-name').textContent);

    const Socket = new WebSocket(
        'ws://' + window.location.host + '/ws/share/' + roomName
    );

    Socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        editor.setValue(data.message);
    };

    Socket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.onkeyup = function(e) {
      if ((e.ctrlKey || e.metaKey) && (e.keyCode === 13 || e.keyCode === 10)) {
            // ctrl+enter to send
            document.querySelector('#chat-message-submit').click();
        }
    };

    document.querySelector('#chat-message-submit').onclick = function(e) {
        const message = editor.getValue();
        Socket.send(JSON.stringify({'message': message}));
    };
});
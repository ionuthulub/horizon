/* global JSEncrypt */
horizon.oslogs = {
    is_paused: false,

    getConsoleLog: function () {
        if ($("#log_tail_length").length == 0) {
            return;
        }
        if (horizon.oslogs.is_paused == false) {
            var form_element = $("#log_tail_length"),
                data;

            data = $(form_element).serialize();

            $.ajax({
                url: $(form_element).attr('action'),
                data: data,
                method: 'get',
                success: function (response_body) {
                    $('pre.logs').text(response_body);
                },
                error: function () {
                    horizon.clearErrorMessages();
                    horizon.alert('error', gettext('There was a problem communicating with the server, please try again.'));
                }
            });
        }
        setTimeout(horizon.oslogs.getConsoleLog, 500);
    }

};

horizon.addInitFunction(horizon.oslogs.init = function () {
    var $document = $(document);

    $document.on('submit', '#log_tail_length', function (evt) {
        if (horizon.oslogs.is_paused) {
            horizon.oslogs.is_paused = false;
            $("#log_tail_length_btn").html("Pause");
        }
        else {
            horizon.oslogs.is_paused = true;
            $("#log_tail_length_btn").html("Play");
        }
        evt.preventDefault();
    });

    horizon.oslogs.getConsoleLog();
});

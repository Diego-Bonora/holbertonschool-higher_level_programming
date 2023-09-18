window.onload = function () {
    $("#btn_translate").click(function () {
        const val = $("#language_code").val()
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${val}`, function (data) {
            $("#hello").text(data["hello"]);
        });
    });
}
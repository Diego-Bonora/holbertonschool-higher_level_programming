window.onload = function () {

    $("#btn_translate").click(function () {
        const val = $("#language_code").val()
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${val}`, function (data) {
            $("#hello").text(data["hello"]);
        });
    });

    $("#language_code").keypress(function (enter) {
        if (enter.key === "Enter") {
            $("#btn_translate").click()
        }
    });
}
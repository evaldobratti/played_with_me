function download_games(url) {
    $.ajax({
        url: url,
        success: function (result) {
            $("#content").prepend(
                "<div class=\"alert alert-success alert-dismissible fade in\" role=\"alert\"> <button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>" + result.message + "</div>"
            )
        },
        error: function (result) {
            alert("Falha " + result.result)
        }
    })
}
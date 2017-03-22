$(document).ready(function () {
    $("#rate-btn").click(function () {
        rating_input = $("#modal-rating-input")
        rating = rating_input.val()
        quote_id = rating_input.data("quote-id")
        $.ajax({
            method: "POST",
            url: "/api/rate_quote/",
            data: {
                "rating": rating,
                "id": quote_id
            }
        })
    })
})
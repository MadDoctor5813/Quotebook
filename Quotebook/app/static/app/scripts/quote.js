update_quote_rating = function (quote_id) {
    display_rating = $(".display-rating[data-quote-id='" + quote_id + "']")
    num_ratings = $(".num-ratings-display[data-quote-id='" + quote_id + "']")
    $.ajax({
        method: "GET",
        url: "/api/get_rating_info/",
        data: {
            "id": quote_id
        },
        success: function (data) {
            display_rating.rating('update', data.rating)
            ratings_text = data.num_ratings + " rating"
            if (data.num_ratings != 1) {
                ratings_text += "s"
            }
            num_ratings.text(ratings_text)
        }
    })
}

$(document).ready(function () {
    $(".rate-btn").click(function (event) {
        //this stops the event triggering for every button
        event.stopImmediatePropagation()
        quote_id = $(this).data("quote-id")
        //find the rating input with the id that matches this button
        rating_input = $(".input-rating[data-quote-id='" + quote_id + "']")
        rating = rating_input.val()
        $.ajax({
            method: "POST",
            url: "/api/rate_quote/",
            data: {
                "rating": rating,
                "id": quote_id,
                "csrfmiddlewaretoken" : CSRF_TOKEN
            },
            success: function () {
                update_quote_rating(quote_id)
            }
        })
        //close the modal ourselves, because we stopped event propagation earlier
        $(this).parents(".modal").modal("hide")
    })
})
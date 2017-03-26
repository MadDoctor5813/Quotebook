update_quote_rating = function (quote_id, rating, num_ratings) {
    display_rating = $(".display-rating[data-quote-id='" + quote_id + "']")
    num_ratings_display = $(".num-ratings-display[data-quote-id='" + quote_id + "']")
    display_rating.rating('update', rating)
    ratings_text = num_ratings + " rating"
    if (num_ratings != 1) {
        ratings_text += "s"
    }
    num_ratings_display.text(ratings_text)
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
            success: function (data) {
                update_quote_rating(quote_id, data.rating, data.num_ratings)
            }
        })
        //close the modal ourselves, because we stopped event propagation earlier
        $(this).parents(".modal").modal("hide")
    })
})
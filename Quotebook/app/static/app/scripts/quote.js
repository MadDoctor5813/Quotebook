update_quote_rating = function (quote_id, rating, num_ratings) {
    quote_well = $(".quote-well[data-quote-id='" + quote_id + "']")
    display_rating = $(quote_well).find(".display-rating")
    num_ratings_display = $(quote_well).find(".num-ratings-display")
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
        var rate_modal = $(this).parents(".modal")
        quote_id = rate_modal.data("quote-id")
        rating_input = rate_modal.find(".input-rating")
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
        rate_modal.modal("hide")
    })
})
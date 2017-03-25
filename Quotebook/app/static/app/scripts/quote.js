$(document).ready(function () {
    $(".rate-btn").click(function (event) {
        //this stops the event triggering for every button
        event.stopImmediatePropagation()
        quote_id = $(this).data("quote-id")
        //find the rating input with the id that matches this button
        rating_input = $(".rating[data-quote-id='" + quote_id + "']")
        rating = rating_input.val()
        $.ajax({
            method: "POST",
            url: "/api/rate_quote/",
            data: {
                "rating": rating,
                "id": quote_id,
                "csrfmiddlewaretoken" : CSRF_TOKEN
            }
        })
        //close the modal ourselves, because we stopped event propagation earlier
        $(this).parents(".modal").modal("hide")
    })
})
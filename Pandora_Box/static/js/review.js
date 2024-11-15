$(document).ready(function() {
    $('#review-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting normally
        var formData = $(this).serialize(); // Serialize form data
        var url = $(this).attr('action'); // Get the form action URL

        // Submit form data via AJAX
        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            success: function(response) {
                // Display an alert indicating successful review submission
                alert('Review submitted successfully');
                // Clear the input field
                $('#review-input').val('');
            },
            error: function(xhr, status, error) {
                console.error('Error submitting review:', error);
            }
        });
    });
});
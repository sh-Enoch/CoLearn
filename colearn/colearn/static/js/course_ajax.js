$(document).ready(function () {
    $('#courseForm').on('submit', function (e) {
        e.preventDefault();

        $.ajax({
            url: '/courses/add/',
            type: 'POST',
            data: $(this).serialize(),  // Serialize form data for submission
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val(),  // CSRF protection
            },
            success: function (response) {
                if (response.success) {
                    $('#courseList').append(response.course_html);  // Add the new course to the list
                    alert('Course added successfully!');
                } else {
                    $('#formErrors').html(response.error_html);  // Display errors
                }
            },
            error: function (xhr) {
                alert('An error occurred: ' + xhr.responseText);
            },
        });
    });
});

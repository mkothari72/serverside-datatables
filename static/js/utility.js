$(document).ready(function () {
    var data_table = $('#example').DataTable({
        columns: [
            { data: 'name'},
            { data: 'position'},
            { data: 'office'},
            { data: 'age'},
            { data: 'start_date'},
            { data: 'salary'},
        ],
    });

    $('#updBtn').click(function () {
        var spinner='<div class="spinner-border  text-light" role="status"><span class="sr-only">Loading...</span></div> Processing ...... '
        $('#updBtn').html(spinner)
        var data = data_table.rows().data();
        alert( 'The table has '+data.length+' records' );
        console.log(JSON.stringify(data)); 
        $.ajax({
            url: "/update",
            type:'POST',
            headers: {
                'X-CSRF-TOKEN': '{{ csrf_token() }}'
            },
            "dataType": "json",
            "data": JSON.stringify(data),
            "contentType": "application/json; charset=utf-8",
            success: function(result) {
                console.log(result)
                alert("Your changes have been committed to the database");
                $('#updBtn').text("Submit form")
                window.location="/";
            },
            error: function(result) {
                $('#updBtn').text("Submit")
                alert('error in POST');
            }
        })    
    });
});


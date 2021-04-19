// clear field value once closed
// $(function () {
//     $('#collapse-search').on('hidden.bs.collapse', function () {
//         $('#search').val('')
//     })
// })

// $(function () {
//     $('select').selectpicker();
// });


function print_div() {

    window.print()
}

function printDiv(divName) {
    var printContents = document.getElementById(divName).innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;

    window.print();

    document.body.innerHTML = originalContents;

}


$("#search-box").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-table tr").filter(function () { //here #table table body id
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
});

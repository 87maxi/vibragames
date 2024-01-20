
$('#exampleModal').on('show.bs.modal', function (event) {
  
  console.log(event)
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
});

function load_data(id){
  $.ajax({
        url: "edit/"+id,
        type: 'GET',
        dataType: 'json',
        success: function(res) {
            console.log(res)
            $("#nombre").val(res.name)
            $("#apellido").val(res.apellido)
            $("#password").val(res.password)
            $("#email").val(res.email)
            $("#birthdate").val(res.birthdate)
            $('#exampleModal form').append( "<input name='id'  id='id_hidden'  type='hidden' value='"+id+"' />" )
            $('#exampleModal').modal('show')
        }
    });
}


function remove_hidden(){

  $('#id_hidden').remove()


}


function delete_element(id){
  
  $.ajax({
        url: "delete/"+id,
        type: 'POST',
        //dataType: 'json',
        success: function(res) {
          console.log(res)
          location.reload();
        }
    });
}


a = function(b){
  data =  JSON.stringify(b)

  console.log(data)

}


function list_elements(){
  
  $(document).ready(function(){

  $.ajax({
        url: "api/v1",
        type: 'GET',
        dataType: 'json',
        success: function(res) {
          a(res)
          
        }
    });

  })
}

list_elements()


//exporte les données sélectionnées
var $table = $('#table');
    $(function () {
        $('#toolbar').find('select').change(function () {
            $table.bootstrapTable('refreshOptions', {
                exportDataType: $(this).val()
            });
        });
    })

		var trBoldBlue = $("table");

	$(trBoldBlue).on("click", "tr", function (){
			$(this).toggleClass("bold-blue");
	});


  $(document).ready(function() {
    var table = $('#vibragames').DataTable({
        searchPanes: true
    });
    table.searchPanes.container().prependTo(table.table().container());
    table.searchPanes.resizePanes();
});
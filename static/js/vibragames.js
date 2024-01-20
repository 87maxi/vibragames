
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
            $('#edit_modal form').append( "<input name='id'  id='id_hidden'  type='hidden' value='"+id+"' />" )
            $('#edit_modal').modal('show')
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
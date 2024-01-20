
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
            console.log(res.name)
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

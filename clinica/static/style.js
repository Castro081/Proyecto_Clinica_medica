
    document.getElementById('submit-btn').addEventListener('click', function() {

        document.getElementById('message-container').innerText = '';
  });

    function showSuccessMessage() {
        document.getElementById('message-container').innerText = '¡Paciente registrado con éxito!';
  }

    function showErrorMessage() {
        document.getElementById('message-container').innerText = 'Error: Revise los campos e inténtelo de nuevo.';
  }


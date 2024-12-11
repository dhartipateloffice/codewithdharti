function copyCode() {
    const codeElement = document.querySelector('pre code');
    navigator.clipboard.writeText(codeElement.innerText);
    alert("Code copied!");
  }

  const copyCodeButtons = document.querySelectorAll('.copy-button');
  copyCodeButtons.forEach(button => {
      button.addEventListener('click', copyCode);
  });





// Open the modal
function openModal(id) {
    var modal = document.getElementById('modal-' + id);
    modal.style.display = "block";
}

// Close the modal
function closeModal(id) {
    var modal = document.getElementById('modal-' + id);
    modal.style.display = "none";
}

// Close the modal when clicking outside the modal content
window.onclick = function(event) {
    var modals = document.getElementsByClassName('modal');
    for (var i = 0; i < modals.length; i++) {
        if (event.target == modals[i]) {
            modals[i].style.display = "none";
        }
    }
}

var quill = new Quill('', {
    theme: 'snow'
  });

  var form = document.querySelector('form');
  form.onsubmit = function() {
    var text = document.querySelector();
    text.value = quill.root.innerHTML;
  };
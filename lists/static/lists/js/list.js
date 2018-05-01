$(document).ready(function() {
  $(':checkbox').on('click', changeTodoStatus);
});

function changeTodoStatus() {
  putNewStatus(this.getAttribute('data-todo-id'), $(this).is(':checked'));
}

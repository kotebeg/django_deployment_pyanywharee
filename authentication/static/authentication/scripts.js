function fillupCredentials() {
    document.getElementById("floatingInput").value = "visitor";
    document.getElementById("floatingPassword").value = "tester123";

    var modal = bootstrap.Modal.getInstance(document.getElementById("credentialsModal"));
    if (modal) {
        modal.hide();
    }
    document.getElementById("floatingInput").focus();
}

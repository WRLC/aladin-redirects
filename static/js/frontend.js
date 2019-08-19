// frontend js functions

// inst form
function submitInst() {
    var base_url = window.location.protocol + "//" + window.location.host + "/";
    var sub_url = 'Z-WEB/Aladin';
    var params = window.location.search;
    var select = document.getElementById('inst');
    var institution = '&inst=' + select.options[select.selectedIndex].value;
    window.location.replace(base_url + sub_url + params + institution);
    return false;
}
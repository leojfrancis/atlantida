$('form#contact-form').submit(submitContactForm);

function submitContactForm(evt) {
    evt.preventDefault();
    $('#form-loading-container').removeClass('d-none')
    $('#form-container').addClass('d-none')
    $('#form-failure-container').addClass('d-none')
    var formData = $('form#contact-form').serializeArray();
    $.ajax('/api/v1/contact-us',{
        method: 'POST',
        data: formData,
        success: (resp) => resp === 'Success' ? onSubmitSuccess() : onSubmitFailure(),
        error: () => onSubmitFailure(),
    });
    return false;
}

function onSubmitSuccess() {
    $('#form-success-container').removeClass('d-none')
    $('#form-loading-container').addClass('d-none')
    $('#form-intro').remove()
    
}
function onSubmitFailure() {
    $('#form-loading-container').addClass('d-none')
    $('#form-container').removeClass('d-none')
    $('#form-failure-container').removeClass('d-none')
    $('#form-intro').remove()
}
const addImageFormBtn = document.querySelector("#add-image-form");
const submitFormBtn = document.querySelector('[type="submit"]');

const imageForm = document.getElementsByClassName("image-form");
const mainForm = document.querySelector("#pet_form");



addImageFormBtn.addEventListener("click", function (event) {
    event.preventDefault();
    // Clone a New Form
    const newImageForm = imageForm[0].cloneNode(true);
    // Insert New Form before the Submit button
    mainForm.insertBefore(newImageForm, submitFormBtn);
});

const totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formCount = imageForm.length - 1;

addImageFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newImageForm = imageForm[0].cloneNode(true);

    const formRegex = RegExp(`form-(\\d){1}-`, 'g');
    formCount++;

    newImageForm.innerHTML = newImageForm.innerHTML.replace(formRegex, `form-${formCount}-`);
    mainForm.insertBefore(newImageForm, submitFormBtn);
    totalForms.setAttribute('value', `${formCount + 1}`);
});
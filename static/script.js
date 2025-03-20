let dropArea = document.getElementById("drop-area");
let fileInput = document.getElementById("imageInput");
let preview = document.getElementById("preview");
let detectBtn = document.getElementById("detectAgeBtn");
let resultDiv = document.getElementById("result");

// Drag & Drop Events
dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("highlight");
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("highlight");
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("highlight");

    let file = e.dataTransfer.files[0];
    if (validateFile(file)) {
        fileInput.files = e.dataTransfer.files; // Set the file in input
        showPreview(file);
    }
});

// Click to Select Image
dropArea.addEventListener("click", () => fileInput.click());

// File Selection Event
fileInput.addEventListener("change", function () {
    let file = fileInput.files[0];
    if (validateFile(file)) {
        showPreview(file);
    }
});

// Validate Image File
function validateFile(file) {
    if (!file) {
        alert("No file selected.");
        return false;
    }

    const validTypes = ["image/jpeg", "image/png", "image/jpg"];
    if (!validTypes.includes(file.type)) {
        alert("Invalid file type. Please select a JPG or PNG image.");
        return false;
    }

    return true;
}

// Show Image Preview
function showPreview(file) {
    let reader = new FileReader();
    reader.onload = function (e) {
        preview.src = e.target.result;
        preview.classList.add("show");
        detectBtn.disabled = false; // Enable button
    };
    reader.readAsDataURL(file);
}

// Upload & Detect Age
function uploadImage() {
    if (fileInput.files.length === 0) {
        alert("Please select an image first.");
        return;
    }

    let formData = new FormData();
    formData.append("image", fileInput.files[0]);

    // Disable button and show loading state
    detectBtn.disabled = true;
    detectBtn.innerText = "Detecting...";
    resultDiv.innerHTML = "<h3>Processing...</h3>";

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = `
            <h3>Predicted Age: ${data.age}</h3>
            <img src="${data.image_url}" alt="Uploaded Image" style="max-width: 100%; height: auto; margin-top: 10px; border-radius: 10px;">
        `;
    })
    .catch(error => {
        console.error("Error:", error);
        resultDiv.innerHTML = "<h3 style='color: red;'>Error detecting age. Please try again.</h3>";
    })
    .finally(() => {
        detectBtn.disabled = false;
        detectBtn.innerText = "Detect Age";
    });
}

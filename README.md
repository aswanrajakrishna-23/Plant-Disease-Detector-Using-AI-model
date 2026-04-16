# Plant Disease Detection Web App

A front-end web application intended for scanning plant leaves, diagnosing plant diseases, and tracking plant health in a personalized garden dashboard.

## 🌿 Features

This project consists of several core sections:
- **Scan Plant (`scan_plant/code.html`)**: Interface for uploading or taking a picture of a plant leaf for disease diagnosis.
- **Diagnosis Results (`diagnosis_results/code.html`)**: Displays the detection results from the AI model, including the disease name, confidence score, treatment recommendations, and prevention plans.
- **My Garden (`my_garden/code.html`)**: A personalized space to keep track of scanned plants and monitor their health status over time.
- **Dashboard (`dashboard/code.html`)**: The main overview interface displaying high-level botanical data and statistics.

## 🚀 Getting Started

Since this is a static frontend project (HTML/CSS/JS), you do not need a complex build process to view the application:

1. **Clone or Download** the repository to your local machine.
2. **Open the Files:** You can double-click on any of the `code.html` files located in their respective folders to open them directly in your web browser.
3. **Live Server:** For the best development experience, open the `Plant Disease` folder in VS Code and use the **Live Server** extension to launch the app locally.

## 🌐 Deployment

You can quickly deploy this stationary frontend using:

### GitHub Pages
1. Push this folder to a new [GitHub](https://github.com/) repository.
2. Navigate to **Settings** > **Pages** in your repository.
3. Select your main branch as the source. Your site will automatically build and publish.

### Netlify Drop
1. Go to [Netlify Drop](https://app.netlify.com/drop).
2. Drag and drop the `Plant Disease` folder onto the browser interface.
3. Your site will be instantly live with a shareable URL.

## 🛠 Integrations (Upcoming/Backend)

*The application interface is structured to be hooked up to a Python (Flask) backend API, which processes image data to return diagnostic predictions.*

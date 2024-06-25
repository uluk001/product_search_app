# product_search_app

## Description

It is a simple search application that allows users to search for similar images by query.


## Installation

1. Clone the repository
```bash
git clone https://github.com/uluk001/product_search_app.git
cd product_search_app
```

2. Set up the virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Set Urls for the images in the `utils/download_images.py` file
```bash
nano utils/download_images.py
```

5. Run the application
```bash
python -m app.main
```

6. Open the browser and go to `http://127.0.0.1:8000/`


## Usage

1. Upload an image using the form on the main page.
2. Click on the `Search` button to search for similar images.
3. Application will search for similar images and display the results with more than 50% similarity.


## Built With

fastapi - The web framework used
uvicorn - ASGI server
torch - PyTorch is an open source machine learning library
torchvision - The torchvision package consists of popular datasets, model architectures, and common image transformations for computer vision
pillow - Python Imaging Library
requests - Python HTTP library
numpy - The fundamental package for scientific computing with Python
scikit-learn - Simple and efficient tools for predictive data analysis


## Contributing

We welcome contributions to the Neocafe project! If you're interested in helping improve Neocafe, please follow these steps:

1. **Fork the repository**: This creates your own copy of the repository where you can make your changes.
2. **Create a new branch**: Use the command `git checkout -b feature/AmazingFeature` to create a new branch for your feature.
3. **Make your changes**: Implement your new feature or bug fix in this branch.
4. **Commit your changes**: Use the command `git commit -m 'Add some AmazingFeature'` to save your changes with a descriptive commit message.
5. **Push the branch**: Use the command `git push origin feature/AmazingFeature` to upload your changes to your forked repository.
6. **Open a Pull Request**: Go to the GitHub page of your forked repository and click on "New pull request" to submit your changes for review.

## Author & Contact

- **Ismailov** - Initial work - [uluk001](https://github.com/uluk001)

If you have questions, suggestions, or would like to report a bug, feel free to contact me at [ulukmanmuratov@gmail.com](mailto:ulukmanmuratov@gmail.com), via Telegram [@ismailovvv001](https://t.me/ismailovvv001), or connect with me on [LinkedIn](https://www.linkedin.com/in/ismailov-uluk-92784a233/).
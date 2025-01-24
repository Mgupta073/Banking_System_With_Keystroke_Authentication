# Banking_System_With_Keystroke_Authentication

This repository contains a project that integrates a banking system with an advanced keystroke authentication mechanism. The primary objective is to enhance the security of user authentication by analyzing keystroke dynamics.

## Features

- **User Registration**: Secure user registration with keystroke pattern recording.
- **Keystroke Authentication**: Analyze typing patterns for added authentication security.
- **Banking Operations**: Basic banking functionalities like account creation, balance inquiry, and transaction history.
- **Data Encryption**: Ensure sensitive user information and keystroke data are encrypted for security.

## Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite for lightweight data management
- **Keystroke Dynamics Analysis**: Libraries such as NumPy and Pandas for data processing

## How It Works

### Registration:
- Users input their username and password.
- Typing patterns (e.g., keypress and release times) are recorded and stored.

### Login:
- Users enter their credentials and repeat their keystroke pattern.
- The system verifies the typing pattern against the stored template for authentication.

### Banking System:
- Access banking functionalities after successful authentication.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Mgupta073/Banking_System_With_Keystroke_Authentication.git
   cd Banking_System_With_Keystroke_Authentication
   
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the application:
   ```bash
   python app.py

5. Access the application at http://localhost:5000

## Future Enhancements
- Integration with cloud-based databases for scalability.
- Machine learning models for enhanced keystroke analysis.
- Mobile-friendly responsive design.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with a detailed description of your changes.



  

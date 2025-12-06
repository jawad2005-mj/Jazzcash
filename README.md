# 💰 JazzCash USSD Simulator

A beautiful and fully responsive Streamlit web application that simulates the JazzCash USSD banking system with smooth animations and modern UI design.

## ✨ Features

- 🎨 **Modern UI Design** - Gradient backgrounds, smooth animations, and responsive layout
- 💸 **Send Money** - Transfer to mobile accounts, CNIC, bank accounts, and Raast/IBAN
- 💡 **Pay Bills** - Pay electricity, gas, water, telephone, internet, and mobile postpaid bills
- 📱 **Load & Bundles** - Transfer mobile load to Jazz, Telenor, Zong, and Ufone
- 💵 **Ready Cash** - Apply for instant loans and manage repayments
- 💳 **Payments** - Government payments, traffic challans, and education fees
- 👤 **My Account** - Check balance, manage MPIN, update email, and debit card services
- 🔒 **Secure** - MPIN validation and transaction verification
- 📱 **Fully Responsive** - Works perfectly on desktop, tablet, and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jazzcash-simulator.git
cd jazzcash-simulator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to:
```
http://localhost:8501
```

## 🎯 How to Use

1. **Start the App** - Enter the USSD code `*786#` to access the main menu
2. **Navigate** - Choose from various services like Send Money, Pay Bills, etc.
3. **Complete Transactions** - Fill in the required details and confirm with your MPIN
4. **Check Balance** - View your current balance in the My Account section

## 🎨 Features Showcase

### Send Money
- Transfer to mobile accounts (11-digit validation)
- Send to CNIC (13-digit validation)
- Bank transfers (16-24 digit account numbers)
- Raast/IBAN transfers

### Pay Bills
- Electricity bills
- Gas bills
- Water bills
- Telephone bills
- Internet bills
- Mobile postpaid bills

### Load & Bundles
- Jazz load transfer
- Telenor load transfer
- Zong load transfer
- Ufone load transfer

### Ready Cash
- Apply for instant loans (Rs. 2,500 - Rs. 5,000)
- Repay loans
- View repayment history

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Language**: Python 3.x
- **Styling**: Custom CSS with animations
- **Fonts**: Google Fonts (Poppins)

## 📱 Responsive Design

The application is fully responsive and works seamlessly across:
- 🖥️ Desktop computers
- 💻 Laptops
- 📱 Tablets
- 📱 Mobile phones

## 🎭 Animations

- Smooth slide-in animations for cards
- Pulse effects for success messages
- Shake effects for error messages
- Hover effects on buttons
- Fade-in animations for page loads

## 🔐 Security Features

- MPIN validation (4-digit)
- Mobile number validation (11-digit)
- CNIC validation (13-digit)
- Reference number validation (15-digit)
- Balance verification before transactions

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy your app by selecting the repository

### Deploy on Heroku

1. Create a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Deploy on Railway

1. Connect your GitHub repository
2. Railway will auto-detect Streamlit
3. Deploy with one click

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created with ❤️ by [jawad2005-mj]

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For any queries or suggestions, feel free to reach out!

## 🙏 Acknowledgments

- JazzCash for the inspiration
- Streamlit for the amazing framework
- Google Fonts for beautiful typography

---

⭐ Star this repo if you find it helpful!


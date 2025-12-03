import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="JazzCash USSD Simulator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        padding: 1rem;
        border-radius: 15px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin: 0.5rem 0;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .jazzcash-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        animation: slideIn 0.5s ease-out;
        margin: 1rem 0;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .success-message {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-weight: 600;
        animation: pulse 0.5s ease-in-out;
        margin: 1rem 0;
    }
    
    .error-message {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-weight: 600;
        animation: shake 0.5s ease-in-out;
        margin: 1rem 0;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        75% { transform: translateX(10px); }
    }
    
    .header-title {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        animation: fadeIn 1s ease-in;
        margin-bottom: 2rem;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.8rem;
        font-size: 1rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'balance' not in st.session_state:
    st.session_state.balance = 50000

def show_success(message):
    st.markdown(f'<div class="success-message">✅ {message}</div>', unsafe_allow_html=True)
    time.sleep(1)

def show_error(message):
    st.markdown(f'<div class="error-message">❌ {message}</div>', unsafe_allow_html=True)

def main_menu():
    st.markdown('<h1 class="header-title">💰 JazzCash</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="jazzcash-card">', unsafe_allow_html=True)
        
        if st.session_state.page == 'home':
            st.markdown("### 📱 Dial USSD Code")
            ussd = st.text_input("Enter USSD Code", placeholder="*786#", key="ussd_input")
            
            if st.button("📞 Dial"):
                if ussd == "*786#":
                    st.session_state.page = 'main_menu'
                    st.rerun()
                else:
                    show_error("Invalid MMI Code")
        
        elif st.session_state.page == 'main_menu':
            st.markdown("### 🏠 Main Menu")
            st.markdown(f"**Balance:** Rs. {st.session_state.balance:,}")
            
            if st.button("💸 1. Send Money"):
                st.session_state.page = 'send_money'
                st.rerun()
            if st.button("💡 2. Pay Bills"):
                st.session_state.page = 'pay_bills'
                st.rerun()
            if st.button("📱 3. Load & Bundles"):
                st.session_state.page = 'load_bundles'
                st.rerun()
            if st.button("💵 4. Ready Cash"):
                st.session_state.page = 'ready_cash'
                st.rerun()
            if st.button("💳 5. Payments"):
                st.session_state.page = 'payments'
                st.rerun()
            if st.button("👤 6. My Account"):
                st.session_state.page = 'my_account'
                st.rerun()
            if st.button("🔙 Exit"):
                st.session_state.page = 'home'
                st.rerun()
        
        elif st.session_state.page == 'send_money':
            send_money_menu()
        
        elif st.session_state.page == 'pay_bills':
            pay_bills_menu()
        
        elif st.session_state.page == 'load_bundles':
            load_bundles_menu()
        
        elif st.session_state.page == 'ready_cash':
            ready_cash_menu()
        
        elif st.session_state.page == 'payments':
            payments_menu()
        
        elif st.session_state.page == 'my_account':
            my_account_menu()
        
        st.markdown('</div>', unsafe_allow_html=True)

def send_money_menu():
    st.markdown("### 💸 Send Money")
    
    option = st.selectbox("Select Option", [
        "To Mobile Account",
        "To CNIC",
        "To Bank",
        "To Raast/IBAN"
    ])
    
    if option == "To Mobile Account":
        mobile = st.text_input("Mobile Number (11 digits)", max_chars=11)
        amount = st.number_input("Amount", min_value=1, max_value=st.session_state.balance)
        password = st.text_input("MPIN (4 digits)", type="password", max_chars=4)
        
        if st.button("Send"):
            if len(mobile) == 11 and len(password) == 4 and mobile.isdigit():
                st.session_state.balance -= amount
                show_success(f"Rs. {amount} sent successfully to {mobile}")
                time.sleep(2)
                st.session_state.page = 'main_menu'
                st.rerun()
            else:
                show_error("Invalid mobile number or MPIN")
    
    elif option == "To CNIC":
        cnic = st.text_input("CNIC (13 digits)", max_chars=13)
        amount = st.number_input("Amount", min_value=1, max_value=st.session_state.balance)
        password = st.text_input("MPIN (4 digits)", type="password", max_chars=4)
        
        if st.button("Send"):
            if len(cnic) == 13 and len(password) == 4 and cnic.isdigit():
                st.session_state.balance -= amount
                show_success(f"Rs. {amount} sent successfully to CNIC {cnic}")
                time.sleep(2)
                st.session_state.page = 'main_menu'
                st.rerun()
            else:
                show_error("Invalid CNIC or MPIN")
    
    elif option == "To Bank":
        bank_account = st.text_input("Bank Account (16-24 digits)", max_chars=24)
        amount = st.number_input("Amount", min_value=1, max_value=st.session_state.balance)
        password = st.text_input("MPIN (4 digits)", type="password", max_chars=4)
        
        if st.button("Send"):
            if len(bank_account) >= 16 and len(password) == 4:
                st.session_state.balance -= amount
                show_success(f"Rs. {amount} sent successfully to bank account")
                time.sleep(2)
                st.session_state.page = 'main_menu'
                st.rerun()
            else:
                show_error("Invalid bank account or MPIN")
    
    if st.button("🔙 Back to Main Menu"):
        st.session_state.page = 'main_menu'
        st.rerun()

def pay_bills_menu():
    st.markdown("### 💡 Pay Bills")
    
    bill_type = st.selectbox("Select Bill Type", [
        "Electricity",
        "Gas",
        "Water",
        "Telephone",
        "Internet",
        "Mobile Postpaid"
    ])
    
    reference_no = st.text_input("Reference Number (15 digits)", max_chars=15)
    amount = st.number_input("Bill Amount", min_value=1)
    password = st.text_input("MPIN (4 digits)", type="password", max_chars=4)
    
    if st.button("Pay Bill"):
        if len(reference_no) == 15 and len(password) == 4:
            if amount <= st.session_state.balance:
                st.session_state.balance -= amount
                show_success(f"{bill_type} bill of Rs. {amount} paid successfully!")
                time.sleep(2)
                st.session_state.page = 'main_menu'
                st.rerun()
            else:
                show_error("Insufficient balance")
        else:
            show_error("Invalid reference number or MPIN")
    
    if st.button("🔙 Back to Main Menu"):
        st.session_state.page = 'main_menu'
        st.rerun()

def load_bundles_menu():
    st.markdown("### 📱 Load & Bundles")
    
    operator = st.selectbox("Select Operator", [
        "Jazz",
        "Telenor",
        "Zong",
        "Ufone"
    ])
    
    mobile = st.text_input("Mobile Number (11 digits)", max_chars=11)
    amount = st.number_input("Load Amount", min_value=10, max_value=5000)
    password = st.text_input("MPIN (4 digits)", type="password", max_chars=4)
    
    if st.button("Transfer Load"):
        if len(mobile) == 11 and len(password) == 4 and mobile.isdigit():
            if amount <= st.session_state.balance:
                st.session_state.balance -= amount
                show_success(f"Rs. {amount} load transferred to {mobile} ({operator})")
                time.sleep(2)
                st.session_state.page = 'main_menu'
                st.rerun()
            else:
                show_error("Insufficient balance")
        else:
            show_error("Invalid mobile number or MPIN")
    
    if st.button("🔙 Back to Main Menu"):
        st.session_state.page = 'main_menu'
        st.rerun()

def ready_cash_menu():
    st.markdown("### 💵 Ready Cash")
    
    st.info("You are eligible for ReadyCash up to Rs. 5,000")
    
    option = st.radio("Select Option", [
        "Apply for Ready Cash",
        "Repay Ready Cash",
        "Repayment History"
    ])
    
    if option == "Apply for Ready Cash":
        loan_amount = st.selectbox("Select Amount", [2500, 3000, 3500, 5000])
        if st.button("Apply"):
            st.session_state.balance += loan_amount
            show_success(f"Loan of Rs. {loan_amount} approved and credited!")
            time.sleep(2)
            st.session_state.page = 'main_menu'
            st.rerun()
    
    elif option == "Repay Ready Cash":
        st.warning("You do not have any outstanding loan to repay")
    
    elif option == "Repayment History":
        st.info("No repayment history available")
    
    if st.button("🔙 Back to Main Menu"):
        st.session_state.page = 'main_menu'
        st.rerun()

def payments_menu():
    st.markdown("### 💳 Payments")
    
    payment_type = st.selectbox("Select Payment Type", [
        "Government Payment",
        "Traffic Challan",
        "Loan Repayment",
        "State Life",
        "Education Payment"
    ])
    
    st.info(f"Selected: {payment_type}")
    st.warning("This feature is under development")
    
    if st.button("🔙 Back to Main Menu"):
        st.session_state.page = 'main_menu'
        st.rerun()

def my_account_menu():
    st.markdown("### 👤 My Account")
    
    option = st.radio("Select Option", [
        "Check Balance",
        "Manage MPIN",
        "Update Email",
        "Debit Card"
    ])
    
    if option == "Check Balance":
        password = st.text_input("Enter MPIN", type="password", max_chars=4)
        if st.button("Check"):
            if len(password) == 4:
                st.success(f"💰 Your balance is: Rs. {st.session_state.balance:,}")
            else:
                show_error("Invalid MPIN")
    
    elif option == "Manage MPIN":
        st.info("MPIN management feature coming soon")
    
    elif option == "Update Email":
        email = st.text_input("Enter Email Address")
        if st.button("Update"):
            if "@" in email and "." in email:
                show_success("Email updated successfully!")
            else:
                show_error("Invalid email address")
    
    elif option == "Debit Card":
        st.info("Debit card services coming soon")
    
    if st.button("🔙 Back to Main Menu"):
        st.session_state.page = 'main_menu'
        st.rerun()

if __name__ == "__main__":
    main_menu()

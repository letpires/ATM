import streamlit as st

# Interface Streamlit
def main():
    st.title("Simulador de ATM")

    menu_options = ["Verificar Saldo", "Depósito", "Retirada", "Histórico de Transações"]
    choice = st.sidebar.selectbox("Menu", menu_options)

    if choice == "Verificar Saldo":
        st.subheader("Verificar Saldo")


    elif choice == "Depósito":
        st.subheader("Realizar Depósito")
        # Lógica para depósito

    elif choice == "Retirada":
        st.subheader("Realizar Retirada")
        # Lógica para retirada

    elif choice == "Histórico de Transações":
        st.subheader("Histórico de Transações")
        # Lógica para exibir histórico

if __name__ == '__main__':
    main()
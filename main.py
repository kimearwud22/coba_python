import streamlit as st
def main():
    st.title("Coffee Website")
    st.write("Welcome to our coffee website! Here, you can explore different coffee types and recipes.")

    # Add navigation options using radio buttons
    navigation = st.radio("Select a page:", ("Home", "Types of Coffee", "Coffee Recipes"))

    # Show content based on the selected page
    if navigation == "Home":
        show_home()
    elif navigation == "Types of Coffee":
        show_coffee_types()
    elif navigation == "Coffee Recipes":
        show_coffee_recipes()

# Define functions for each page
def show_home():
    st.header("Home")
    st.write("Welcome to the Home page. Here, you can find information about coffee.")

def show_coffee_types():
    st.header("Types of Coffee")
    st.write("Here are some popular types of coffee:")
    st.write("- Espresso")
    st.write("- Cappuccino")
    st.write("- Latte")
    st.write("- Americano")
    st.write("- Mocha")

def show_coffee_recipes():
    st.header("Coffee Recipes")
    st.write("Here are some coffee recipes:")
    st.write("- Espresso Martini")
    st.write("- Iced Caramel Latte")
    st.write("- Cinnamon Dolce Latte")
    st.write("- Cold Brew Coffee")
    st.write("- Irish Coffee")

# Call the main function to run the app
if __name__ == "__main__":
    main()

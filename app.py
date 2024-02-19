
import streamlit as st
import random

def roll_dice(num_dice, no_sides):
    rolls = [random.randint(1, no_sides) for _ in range(num_dice)]
    return rolls

def main():
    st.title('Dice Roller')

    num_dice = st.number_input('Enter the number of dice:', min_value=1, step=1)
    no_sides = st.number_input('Enter the number of sides on each die:', min_value=2, step=1)

    if st.button('Roll Dice'):
        rolls = roll_dice(num_dice, no_sides)
        total = sum(rolls)
        st.write(f"Rolls: {rolls}")
        st.write(f"Total: {total}")

if __name__ == "__main__":
    main()

]
]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
]]]]]]]]]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
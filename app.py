import streamlit as st

# Initialize session state for the board
if 'board' not in st.session_state:
    st.session_state.board = [' ']*9
    st.session_state.current_player = 'X'
    st.session_state.winner = None

def check_winner(board):
    # Winning combinations
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def make_move(pos):
    if st.session_state.board[pos] == ' ' and st.session_state.winner is None:
        st.session_state.board[pos] = st.session_state.current_player
        winner = check_winner(st.session_state.board)
        if winner:
            st.session_state.winner = winner
        else:
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

def reset_game():
    st.session_state.board = [' ']*9
    st.session_state.current_player = 'X'
    st.session_state.winner = None

st.title("Tic Tac Toe 🟢❌")

# Display winner
if st.session_state.winner:
    st.success(f"Player {st.session_state.winner} wins!")
elif ' ' not in st.session_state.board:
    st.info("It's a Draw!")

# Create board layout
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        pos = i*3 + j
        if cols[j].button(st.session_state.board[pos], key=pos):
            make_move(pos)

st.button("Reset Game 🔄", on_click=reset_game)

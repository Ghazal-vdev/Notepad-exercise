from MyNotes import NoteManager
import streamlit as st

st.set_page_config(page_title='My Notepad', page_icon='📝', layout="centered")

manager = NoteManager() # making object from class

st.title("**My Notepad Application📝**")
menu = st.sidebar.selectbox("Menu Selection",["Search","Add note", "Edit note", "Delete note","Show notes"])

# ------------------ADD----------------------------------------------------------------

if menu == 'Add note':
   st.subheader('New note ✍🏻')
   note = st.text_area("Write as you wish",placeholder="Start unperfect...", height=150)
   if st.button("Save"):
        if note:
            success = manager.add_note(note)
            if success:
              st.success("Saved.✅")
              st.balloons()
            else:
                st.error("Something went wrong in saving.")
        else:
            st.warning("Please write something.")

# -----------------EDIT-----------------------------------------------------------------

elif menu == 'Edit note':
   st.subheader("Edit a note ✏")
   notes = manager.show_notes()
   if not notes:
    st.info("No notes to edit.")
   else:
        note_options = {f"{n[1]} (ID: {n[0]})": n[0] for n in notes}
        selected_note_label = st.selectbox("Which note do you want to edit?", list(note_options.keys()))
        selected_note_id = note_options[selected_note_label]
        current_note_content = ""
        for n in notes:
            if n[0] == selected_note_id:
                current_note_content = n[1]
                break

        new_content = st.text_area("Edit content:", value=current_note_content, height=150)

        if st.button("Save Changes"):
            if new_content:
                success, msg = manager.edit_note(selected_note_id, new_content)
                if success:
                    st.success("Updated successfully! 🎉")
                    st.rerun()
                else:
                    st.error(msg)
            else:
                st.warning("Content cannot be empty!")

# --------------------DELETE---------------------------------------------------

elif menu == 'Delete note':
   st.subheader("Delete a Note 🗑️")
   notes = manager.show_notes()
   if not notes:
    st.info("Nothing to delete.")
   else:
      for note in notes:
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(f"**{note[1]}**")
            with col2:
                if st.button("Delete", key=f"del_{note[0]}"):
                    success, msg = manager.delete_note(note[0])
                    if success:
                        st.success("Deleted!")
                        st.rerun() # for instant list update
                    else:
                        st.error(msg)

# ----------------------SHOW----------------------------------------------------

elif menu == 'Show notes':
   st.subheader("All notes 📓")
   notes = manager.show_notes()
   if not notes:
      st.info("You haven't saved any notes. 😴")
   else:
       if len(notes) > 0:
            for note in notes:
                with st.expander(f"📝 {note[1][:30]}..."):
                    st.write(f"**Full Content:**")
                    st.write(note[1])
                    st.caption(f"Created at: {note[2]}")

                    col1, col2 = st.columns(2)
                    with col2:
                        if st.button("Delete", key=f"del_{note[0]}"):
                            success, msg = manager.delete_note(note[0])
                            if success:
                                st.success("Deleted!")
                                st.rerun()
                            else:
                                st.error(msg)
       else:
           st.info("No notes found in database.")            


# -------------------SEARCH--------------------------------------------------------------

else:
   st.subheader("Searching 🔍")
   query = st.text_input("Enter your term: ")
   if query:
      results = manager.search_note(query)
      if results:
         st.write(f"Found {len(results)} results.")
         for res in results:
            st.write(f"- {res[1]}   ({res[2]})")
      else:
         st.warning("Found no match.")

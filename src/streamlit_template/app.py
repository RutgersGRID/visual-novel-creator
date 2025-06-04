"""Visual Novel Script Creator - Main Streamlit application module."""

import streamlit as st
import pandas as pd
from typing import Dict, List, Any
import json

from streamlit_template.utils import (
    create_character, 
    create_story_arc, 
    create_milestone,
    generate_dialogue_options,
    export_script_format
)


def initialize_session_state():
    """Initialize session state variables."""
    if 'characters' not in st.session_state:
        st.session_state.characters = []
    if 'story_arcs' not in st.session_state:
        st.session_state.story_arcs = []
    if 'milestones' not in st.session_state:
        st.session_state.milestones = []
    if 'dialogue_scenes' not in st.session_state:
        st.session_state.dialogue_scenes = []
    if 'story_concept' not in st.session_state:
        st.session_state.story_concept = ""


def main() -> None:
    """Main Visual Novel Script Creator application entry point."""
    st.set_page_config(
        page_title="Visual Novel Script Creator", 
        page_icon="📚", 
        layout="wide"
    )

    initialize_session_state()

    st.title("📚 Visual Novel Script Creator")
    st.write("Transform your story ideas into structured visual novel scripts with characters, dialogue branches, and story arcs!")

    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Story Concept", 
        "👥 Characters", 
        "🎭 Story Arcs", 
        "🎯 Milestones", 
        "💬 Dialogue & Export"
    ])

    with tab1:
        story_concept_section()

    with tab2:
        characters_section()

    with tab3:
        story_arcs_section()

    with tab4:
        milestones_section()

    with tab5:
        dialogue_and_export_section()


def story_concept_section():
    """Handle the story concept input section."""
    st.header("Story Concept")
    
    concept = st.text_area(
        "Describe your visual novel concept:",
        value=st.session_state.story_concept,
        height=150,
        help="Provide a general overview of your story idea, setting, genre, and main themes."
    )
    
    if st.button("Save Concept"):
        st.session_state.story_concept = concept
        st.success("Story concept saved!")

    if concept:
        st.subheader("Story Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Word Count:**", len(concept.split()))
            st.write("**Character Count:**", len(concept))
        
        with col2:
            # Simple genre detection based on keywords
            genres = []
            if any(word in concept.lower() for word in ['love', 'romance', 'heart']):
                genres.append("Romance")
            if any(word in concept.lower() for word in ['mystery', 'detective', 'crime']):
                genres.append("Mystery")
            if any(word in concept.lower() for word in ['magic', 'fantasy', 'dragon']):
                genres.append("Fantasy")
            if any(word in concept.lower() for word in ['school', 'student', 'class']):
                genres.append("Slice of Life")
            
            if genres:
                st.write("**Detected Genres:**", ", ".join(genres))


def characters_section():
    """Handle the character creation and management section."""
    st.header("Character Development")

    # Character creation form
    with st.expander("➕ Add New Character", expanded=False):
        with st.form("character_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                char_name = st.text_input("Character Name*")
                char_role = st.selectbox(
                    "Role", 
                    ["Main Character", "Love Interest", "Rival", "Friend", "Mentor", "Antagonist", "Supporting"]
                )
                char_age = st.number_input("Age", min_value=10, max_value=100, value=18)
            
            with col2:
                char_personality = st.text_area("Personality Traits", height=100)
                char_background = st.text_area("Background", height=100)
                char_goals = st.text_area("Goals/Motivations", height=100)

            submitted = st.form_submit_button("Add Character")
            
            if submitted and char_name:
                character = create_character(
                    char_name, char_role, char_age, 
                    char_personality, char_background, char_goals
                )
                st.session_state.characters.append(character)
                st.success(f"Added character: {char_name}")
                st.rerun()

    # Display existing characters
    if st.session_state.characters:
        st.subheader("Your Characters")
        
        for i, char in enumerate(st.session_state.characters):
            with st.expander(f"{char['name']} ({char['role']})"):
                col1, col2, col3 = st.columns([2, 2, 1])
                
                with col1:
                    st.write(f"**Age:** {char['age']}")
                    st.write(f"**Personality:** {char['personality']}")
                
                with col2:
                    st.write(f"**Background:** {char['background']}")
                    st.write(f"**Goals:** {char['goals']}")
                
                with col3:
                    if st.button(f"Delete", key=f"del_char_{i}"):
                        st.session_state.characters.pop(i)
                        st.rerun()


def story_arcs_section():
    """Handle story arc creation and management."""
    st.header("Story Arcs")

    # Story arc creation form
    with st.expander("➕ Create New Story Arc", expanded=False):
        with st.form("arc_form"):
            arc_name = st.text_input("Arc Name*")
            arc_description = st.text_area("Description", height=100)
            
            col1, col2 = st.columns(2)
            with col1:
                arc_start = st.number_input("Start Chapter", min_value=1, value=1)
                arc_themes = st.text_input("Themes/Keywords")
            
            with col2:
                arc_end = st.number_input("End Chapter", min_value=1, value=5)
                
                # Character involvement
                if st.session_state.characters:
                    char_names = [char['name'] for char in st.session_state.characters]
                    involved_chars = st.multiselect("Characters Involved", char_names)
                else:
                    involved_chars = []

            submitted = st.form_submit_button("Create Arc")
            
            if submitted and arc_name:
                arc = create_story_arc(
                    arc_name, arc_description, arc_start, arc_end, 
                    arc_themes, involved_chars
                )
                st.session_state.story_arcs.append(arc)
                st.success(f"Created story arc: {arc_name}")
                st.rerun()

    # Display existing arcs
    if st.session_state.story_arcs:
        st.subheader("Your Story Arcs")
        
        for i, arc in enumerate(st.session_state.story_arcs):
            with st.expander(f"{arc['name']} (Ch. {arc['start_chapter']}-{arc['end_chapter']})"):
                col1, col2, col3 = st.columns([2, 2, 1])
                
                with col1:
                    st.write(f"**Description:** {arc['description']}")
                    st.write(f"**Themes:** {arc['themes']}")
                
                with col2:
                    if arc['characters']:
                        st.write(f"**Characters:** {', '.join(arc['characters'])}")
                    st.write(f"**Duration:** {arc['end_chapter'] - arc['start_chapter'] + 1} chapters")
                
                with col3:
                    if st.button(f"Delete", key=f"del_arc_{i}"):
                        st.session_state.story_arcs.pop(i)
                        st.rerun()


def milestones_section():
    """Handle milestone creation and management."""
    st.header("Story Milestones")

    # Milestone creation form
    with st.expander("➕ Add New Milestone", expanded=False):
        with st.form("milestone_form"):
            milestone_name = st.text_input("Milestone Name*")
            milestone_description = st.text_area("Description", height=100)
            
            col1, col2 = st.columns(2)
            with col1:
                milestone_chapter = st.number_input("Chapter Number", min_value=1, value=1)
                milestone_type = st.selectbox(
                    "Milestone Type",
                    ["Plot Point", "Character Development", "Relationship Change", "World Building", "Conflict Resolution"]
                )
            
            with col2:
                milestone_impact = st.selectbox(
                    "Impact Level",
                    ["Low", "Medium", "High", "Critical"]
                )
                
                # Related arc selection
                if st.session_state.story_arcs:
                    arc_names = [arc['name'] for arc in st.session_state.story_arcs]
                    related_arc = st.selectbox("Related Arc (Optional)", ["None"] + arc_names)
                else:
                    related_arc = "None"

            submitted = st.form_submit_button("Add Milestone")
            
            if submitted and milestone_name:
                milestone = create_milestone(
                    milestone_name, milestone_description, milestone_chapter,
                    milestone_type, milestone_impact, related_arc if related_arc != "None" else None
                )
                st.session_state.milestones.append(milestone)
                st.success(f"Added milestone: {milestone_name}")
                st.rerun()

    # Display existing milestones
    if st.session_state.milestones:
        st.subheader("Your Milestones")
        
        # Sort milestones by chapter
        sorted_milestones = sorted(st.session_state.milestones, key=lambda x: x['chapter'])
        
        for i, milestone in enumerate(sorted_milestones):
            with st.expander(f"Ch. {milestone['chapter']}: {milestone['name']} [{milestone['impact']}]"):
                col1, col2, col3 = st.columns([2, 2, 1])
                
                with col1:
                    st.write(f"**Type:** {milestone['type']}")
                    st.write(f"**Description:** {milestone['description']}")
                
                with col2:
                    st.write(f"**Impact:** {milestone['impact']}")
                    if milestone['related_arc']:
                        st.write(f"**Related Arc:** {milestone['related_arc']}")
                
                with col3:
                    milestone_idx = st.session_state.milestones.index(milestone)
                    if st.button(f"Delete", key=f"del_milestone_{milestone_idx}"):
                        st.session_state.milestones.pop(milestone_idx)
                        st.rerun()


def dialogue_and_export_section():
    """Handle dialogue creation and script export."""
    st.header("Dialogue Scenes & Export")

    # Quick dialogue scene creator
    with st.expander("➕ Create Dialogue Scene", expanded=False):
        scene_name = st.text_input("Scene Name")
        scene_chapter = st.number_input("Chapter", min_value=1, value=1)
        
        if st.session_state.characters:
            char_names = [char['name'] for char in st.session_state.characters]
            scene_characters = st.multiselect("Characters in Scene", char_names)
            
            if scene_characters:
                st.subheader("Dialogue Options")
                dialogue_text = st.text_area("Main Dialogue", height=100)
                
                # Branching options
                num_branches = st.slider("Number of Response Branches", 1, 4, 2)
                branches = []
                
                for i in range(num_branches):
                    branch_text = st.text_input(f"Branch {i+1} Option")
                    if branch_text:
                        branches.append(branch_text)
                
                if st.button("Add Scene"):
                    scene = {
                        'name': scene_name,
                        'chapter': scene_chapter,
                        'characters': scene_characters,
                        'dialogue': dialogue_text,
                        'branches': branches
                    }
                    st.session_state.dialogue_scenes.append(scene)
                    st.success(f"Added scene: {scene_name}")

    # Export section
    st.subheader("Export Your Script")
    
    if (st.session_state.characters or st.session_state.story_arcs or 
        st.session_state.milestones or st.session_state.dialogue_scenes):
        
        col1, col2 = st.columns(2)
        
        with col1:
            export_format = st.selectbox(
                "Export Format",
                ["JSON", "Markdown", "CSV Summary"]
            )
        
        with col2:
            if st.button("Generate Export"):
                export_data = export_script_format(
                    st.session_state.story_concept,
                    st.session_state.characters,
                    st.session_state.story_arcs,
                    st.session_state.milestones,
                    st.session_state.dialogue_scenes,
                    export_format
                )
                
                st.download_button(
                    f"Download {export_format} File",
                    export_data,
                    f"visual_novel_script.{export_format.lower()}",
                    f"text/{export_format.lower()}"
                )

        # Project summary
        st.subheader("Project Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Characters", len(st.session_state.characters))
        with col2:
            st.metric("Story Arcs", len(st.session_state.story_arcs))
        with col3:
            st.metric("Milestones", len(st.session_state.milestones))
        with col4:
            st.metric("Dialogue Scenes", len(st.session_state.dialogue_scenes))

    else:
        st.info("Create some characters, story arcs, or milestones to enable export functionality.")


if __name__ == "__main__":
    main()